import pymonetdb
import unicodedata
import psycopg2
import os
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import unicodedata
import codecs

with codecs.open('data/stopwords.data', encoding='utf-8', mode='r') as f:
	stop_words = [str(x).replace("\n", "").strip().lower() for x in f]

monetConn = pymonetdb.connect(username="paulo", password=os.environ["DB_PASSWORD"],
                               hostname="localhost", database="demo")
monetCur = monetConn.cursor()

conn = psycopg2.connect(database="postgres", user="postgres", password=os.environ["DB_PASSWORD"]) 
cur = conn.cursor()	


def tokenize_tweet(text):
	global stop_words
	text = text.lower()
	tokenizer = TweetTokenizer()
	tokens = tokenizer.tokenize(text)
	tokens = [tok for tok in tokens if tok not in stop_words and not tok.isdigit()]
	return tokens

def closeDatabases():
	print("Closing the database...")
	conn.rollback()
	cur.close()
	conn.close()
	monetCur.close()
	monetConn.close()

def strip_accents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


cur.execute("select t_id, raw_text, u_id from \"Tweet\";")

def addToMonetDB(tokens, tableName, id):

	try:

		monetCur.execute("INSERT INTO " +  tableName + " ("+ id[0] + ") values (" + id[1] + ");")
		monetConn.commit()

	except pymonetdb.exceptions.OperationalError as e:
		monetConn.rollback()
		return

	for t in tokens:
		try:
			st = strip_accents(t)
		except UnicodeDecodeError as e:
			continue
		print("TOKEN : ", st)
		try:
			monetCur.execute('ALTER TABLE ' + tableName + ' ADD ' + st + ' int default 0')
			monetConn.commit()
		except pymonetdb.exceptions.OperationalError as e:
			monetConn.rollback()
			if(('42000' not in str(e)) and ('42S21' in str(e))):
				try:
					monetCur.execute("UPDATE " +  tableName + " SET " + st + " = " + st + " + 1 WHERE " +  id[0] + " = " + id[1])
				except UnicodeDecodeError as e:
					continue
				monetConn.commit()
		except UnicodeDecodeError as e:
			continue

row = cur.fetchone()
while row:
	t_id = str(row[0])
	raw_text = row[1]
	u_id = str(row[2])
	tokens = tokenize_tweet(raw_text)
	print(raw_text)

	addToMonetDB(tokens, "user_tokens", ("u_id", u_id))
	addToMonetDB(tokens, "tweet_tokens", ("t_id", u_id))

	row = cur.fetchone()

closeDatabases()