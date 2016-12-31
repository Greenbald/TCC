import pymonetdb
import unicodedata
import psycopg2
import os
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import codecs
from util import narcissism_classifier
from util import text_processor
import time

TWEETS = 1000

monetConn = pymonetdb.connect(username="paulo", password=os.environ["DB_PASSWORD"],
                               hostname="localhost", database="demo")
monetCur = monetConn.cursor()

conn = psycopg2.connect(database="postgres", user="postgres", password=os.environ["DB_PASSWORD"]) 
cur = conn.cursor()	


def closeDatabases():
	print("Closing the database...", end='\n')
	cur.close()
	conn.close()
	monetConn.commit()
	monetCur.close()
	monetConn.close()


#cur.execute("select t_id, raw_text, u_id from \"Tweet\";")
cur.execute("select t_id, raw_text, u_id from \"Tweet\" order by u_id desc limit " + str(TWEETS))

def addToMonetDB(tokens, tableName, id, classification):

	start_time = time.time()
	try:
		query = "INSERT INTO " +  tableName + " ("+ id[0] + ", classification) values (" + str(id[1]) + "," + str(classification) + ");"
		monetCur.execute(query)
		monetConn.commit()
	except pymonetdb.exceptions.OperationalError as e:
		monetConn.rollback()
		return

	print("R TIME: %s seconds" % (time.time() - start_time))

	start_time = time.time()
	for t in tokens:
		try:
			monetCur.execute('ALTER TABLE ' + tableName + ' ADD ' + t + ' int default 0')
			monetConn.commit()
		except pymonetdb.exceptions.OperationalError as e:
			monetConn.rollback()
			if(('42000' not in str(e)) and ('42S21' in str(e))):
				monetCur.execute("UPDATE " +  tableName + " SET " + t + " = " + t + " + 1 WHERE " +  id[0] + " = " + str(id[1]))
				monetConn.commit()
		except UnicodeDecodeError as e:
			continue

	print("C TIME : %s seconds" % (time.time() - start_time))

row = cur.fetchone()
last_u_id = int(row[2])
user_tweets = 0
user_narcissist_tweets = 0
user_tokens = []

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

	print("U_ID", u_id)
	print("Progresso :", str(total_tweets/TWEETS) + "%", end='\r')

	tokens = text_processor.tokenize_tweet(raw_text)
	new_tokens = text_processor.process_tokens(tokens)

	tweet_classification = narcissism_classifier.classify_tweet(new_tokens)

	#Tweets database
	tweet_classification = narcissism_classifier.classify_tweet(new_tokens)
	addToMonetDB(new_tokens, "tweet_tokens", ("t_id", t_id), tweet_classification)
	if tweet_classification:
		narcissists_tweets = narcissists_tweets + 1

	#Users database
	if last_u_id == u_id:
		user_tokens = user_tokens + new_tokens
		user_tweets = user_tweets + 1
		if narcissism_classifier.classify_tweet(new_tokens):
			user_narcissist_tweets = user_narcissist_tweets + 1
	else:
		total_users = total_users + 1
		if user_narcissist_tweets/user_tweets >= 0.5:
			narcissists_users = narcissists_users + 1
			addToMonetDB(user_tokens, "user_tokens", ("u_id", last_u_id), True)
		else:
			addToMonetDB(user_tokens, "user_tokens", ("u_id", last_u_id), False)
		last_u_id = u_id
		user_narcissist_tweets = 0
		user_tweets = 1
		user_tokens = new_tokens
		if narcissism_classifier.classify_tweet(new_tokens):
			user_narcissist_tweets = user_narcissist_tweets + 1

	#print("Tweet numero : ", total_tweets)
	row = cur.fetchone()

print("TWEETS NARCISISTAS : ", narcissists_tweets/total_tweets)
print("USUARIOS NARCISISTAS : ", narcissists_users/total_users)

closeDatabases()