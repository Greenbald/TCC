import pymonetdb
import unicodedata
import psycopg2
import os
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import unicodedata
import codecs
from util import narcissism_classifier
from util import text_processor
import time


monetConn = pymonetdb.connect(username="paulo", password=os.environ["DB_PASSWORD"],
                               hostname="localhost", database="demo")
monetCur = monetConn.cursor()

conn = psycopg2.connect(database="postgres", user="postgres", password=os.environ["DB_PASSWORD"]) 
cur = conn.cursor()	


def closeDatabases():
	print("Closing the database...")
	cur.close()
	conn.close()
	monetConn.commit()
	monetCur.close()
	monetConn.close()

def strip_accents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


#cur.execute("select t_id, raw_text, u_id from \"Tweet\";")
cur.execute("select t_id, raw_text, u_id from \"Tweet\" order by u_id desc limit 10000")

def addToMonetDB(tokens, tableName, id, classification, text=None):

	user_query = text is None
	start_time = time.time()
	try:
		if not user_query:
			query = "INSERT INTO " +  tableName + " ("+ id[0] + ", classification, text" + ") values (" + str(id[1]) + "," + str(classification) + "," + "'" + text + "');"
		else:
			query = "INSERT INTO " +  tableName + " ("+ id[0] + ", classification) values (" + str(id[1]) + "," + str(classification) + ");"
		monetCur.execute(query)
		monetConn.commit()

	except pymonetdb.exceptions.OperationalError as e:
		monetConn.rollback()
		return
	print("TIME1: %s seconds" % (time.time() - start_time))

	start_time = time.time()
	for t in tokens:
		try:
			st = strip_accents(t)
		except UnicodeDecodeError as e:
			continue
		try:
			monetCur.execute('ALTER TABLE ' + tableName + ' ADD ' + st + ' int default 0')
			monetConn.commit()
		except pymonetdb.exceptions.OperationalError as e:
			monetConn.rollback()
			if(('42000' not in str(e)) and ('42S21' in str(e))):
				try:
					monetCur.execute("UPDATE " +  tableName + " SET " + st + " = " + st + " + 1 WHERE " +  id[0] + " = " + str(id[1]))
				except UnicodeDecodeError as e:
					continue
				monetConn.commit()
				message = "Row added to "
				if user_query:
					message = message + "user_tokens table..."
				else:
					message = message + "tweet_tokens table..."
				#print(message)
		except UnicodeDecodeError as e:
			continue

	print("TIME2: %s seconds" % (time.time() - start_time))

row = cur.fetchone()
last_u_id = int(row[2])
user_classification = False

#Statistics variables
narcissists_tweets = 0
total_tweets = 1
narcissists_users = 0
total_users = 1

while row:
	t_id = int(row[0])
	raw_text = str(row[1])
	u_id = int(row[2])
	total_tweets = total_tweets + 1
	print(u_id)
	tokens = text_processor.tokenize_tweet(raw_text)

	#Tweets database
	tweet_classification = narcissism_classifier.classify_tweet(tokens)
	addToMonetDB(tokens, "tweet_tokens", ("t_id", t_id), tweet_classification, raw_text)
	if tweet_classification:
		narcissists_tweets = narcissists_tweets + 1

	#Users database
	if last_u_id == u_id:
		user_classification = narcissism_classifier.classify_tweet(tokens) or user_classification
	else:
		total_users = total_users + 1
		if user_classification:
			narcissists_users = narcissists_users + 1
		addToMonetDB(tokens, "user_tokens", ("u_id", last_u_id), user_classification)
		last_u_id = u_id
		user_classification = narcissism_classifier.classify_tweet(tokens)

	print("Tweet numero : ", total_tweets)
	row = cur.fetchone()

print("TWEETS NARCISISTAS :", narcissists_tweets/total_tweets)
print("USUARIOS NARCISISTAS : ", narcissists_users/total_users)

closeDatabases()