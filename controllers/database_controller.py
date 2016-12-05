import psycopg2
import sys
import os
import pymonetdb
import unicodedata

conn = None
cur = None
count = 0

monetConn = None
monetCur = None

def open_database_connection():
	print("Connecting to the database...")
	global conn
	conn = psycopg2.connect(database="postgres", user="postgres", password=os.environ["DB_PASSWORD"]) 
	global cur
	cur = conn.cursor()	
	global monetConn
	monetConn = pymonetdb.connect(username="paulo", password=os.environ["DB_PASSWORD"],
                               hostname="localhost", database="demo")
	global monetCur
	monetCur = monetConn.cursor()



def commit():
	if(conn is not None):
		global count
		count += 1
		if(count == 100):
			print("Commiting all data...")
			count = 0
		conn.commit()

def close():
	if((conn  is not None) and (cur is not None)):
		print("Closing the database...")
		conn.rollback()
		cur.close()
		conn.close()
		monetCur.close()
		monetConn.close()

def rollback():
	if((conn is not None)):
		conn.rollback()


def insert_data(tweet, user):
	try:
		u_id = insert_or_update_user(user)

		t_id = insert_tweet(tweet)

		insert_hashtags_and_relationship_with_tweet_if_tweet(t_id, tweet.get_entities())

		#insert_user_tweet_relationship(u_id, t_id)

		monet_insert_tweet(tweet)

		commit()

	except psycopg2.Error as e:
		print(e.pgerror)
		conn.rollback()

def insert_or_update_user(user):
	u_id = verify_user_existence_in_database(user)
	if(u_id < 0):
		u_id = insert_user(user)
	else:
		update_user(user)
	return u_id

def verify_user_existence_in_database(user):
	#cur.execute("select exists(select 1 from \"User\" where \"u_id\"="+ str(user.get_user_id()) + ");")
	cur.execute("select id from \"User\" where \"u_id\" =" + str(user.get_user_id()) + ";")
	row = cur.fetchone()
	if(row is None):
		return -1
	else:
		return row[0]

def insert_user(user):
	if(cur is not None):
		cur.execute(
     		 """INSERT INTO \"User\" (u_id, description, location, followers_count, friends_count)
         	VALUES (%s, %s, %s , %s, %s) RETURNING id;""",
     			(user.get_user_id(), user.get_description(), 
     			user.get_location(), user.get_followers_count(), user.get_friends_count()))
		return cur.fetchone()[0]
	return -1

def update_user(user):
	cur.execute("""UPDATE "User"
   				SET friends_count=%s, description=%s, location=%s, followers_count=%s
   				WHERE u_id =%s;""", (user.get_friends_count(), user.get_description(),
   									user.get_location(), user.get_followers_count(),
   									user.get_user_id()))

def insert_tweet(tweet):
	if(cur is not None):
		cur.execute(
     		 """INSERT INTO \"Tweet\" (t_id, created_at, u_id, text, source, raw_text, date)
         	VALUES (%s, %s, %s , %s, %s, %s, %s) RETURNING id;""",
     			(tweet.get_tweet_id(), tweet.get_created_at(), 
     			tweet.get_user_id(), tweet.get_text(), tweet.get_source_device(),
     			tweet.get_raw_text(), tweet.get_date()))
		return cur.fetchone()[0]
	return -1

def insert_hashtags_and_relationship_with_tweet_if_tweet(t_id, entities):
	if(t_id >= 0):
		h_ids = insert_hashtags(entities.get_hashtags())
		insert_tweet_hashtags(t_id, h_ids)


def insert_hashtags(hashtags):
	""" This function insert the new hashtag in the database or updates
		an old one to increase its count. The return value is an array
		containing all related hashtags """
	ids = []
	if(cur is not None):
		for ht in hashtags:
			tup = get_hashtag_tuple(ht.lower())
			if(tup is None):
				cur.execute(
					"""INSERT INTO "Hashtag" (text) VALUES('{0}') RETURNING id;""".format(ht.lower()))
				h_id = cur.fetchone()[0]
				ids.append(h_id)
			else:
				update_hashtag_count(tup)
				h_id = tup[0]
				ids.append(h_id)
	return ids

def get_hashtag_tuple(hashtag):
	cur.execute("""SELECT id, count FROM "Hashtag" WHERE text='{0}';""".format(hashtag))
	result = cur.fetchone()
	if(result is not None):
		return result
	else:
		result

def update_hashtag_count(tup):
	if(cur is not None):
		count = str(int(tup[1]) + 1)
		cur.execute("""UPDATE "Hashtag" SET count=%s WHERE id=%s;""",
					(count, tup[0]))

def insert_tweet_hashtags(t_id, h_ids):
	if(cur is not None):
		h_ids = list(set(h_ids))
		for i in h_ids:
			cur.execute(
				"""INSERT INTO "Tweet_Hashtag" (t_id, h_id) VALUES(%s, %s);""",
				(t_id, i))

def insert_user_tweet_relationship(u_id, t_id):
	cur.execute(
		"""INSERT INTO "Tweet_User" (t_id, u_id) VALUES(%s, %s);""",
			(t_id, u_id))


#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------MONET DB BELOW-------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------


def strip_accents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def monet_insert_tweet(tweet):

	t_id = tweet.get_tweet_id()

	try:

		monetCur.execute("INSERT INTO tweet_tokens (t_id) values (" + t_id + ");")
		monetConn.commit()

	except pymonetdb.exceptions.OperationalError as e:
		monetConn.rollback()
		return

	for t in tweet.get_tokens():
		try:
			st = strip_accents(t)
		except UnicodeDecodeError as e:
			continue

		print("TOKEN : ", st)
		try:
			monetCur.execute('ALTER TABLE tweet_tokens ADD ' + st + ' int default 0')
			monetConn.commit()
		except pymonetdb.exceptions.OperationalError as e:
			monetConn.rollback()
			if(('42000' not in str(e)) and ('42S21' in str(e))):
				try:
					monetCur.execute("UPDATE tweet_tokens SET " + st + " = " + st + " + 1 WHERE t_id = " + t_id)
				except UnicodeDecodeError as e:
					continue
				monetConn.commit()
		except UnicodeDecodeError as e:
			continue