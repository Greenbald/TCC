import psycopg2

conn = None
cur = None
count = 0

def open_database_connection():
	print("Connecting to the database...")
	global conn
	conn = psycopg2.connect("dbname = tweeling user=postgres")
	global cur
	cur = conn.cursor()

def commit_batch_if_threshold():
	global count
	count += 1
	if(count == 100):
		commit()
		count = 0

def commit():
	if(conn is not None):
		print("Commiting all data...")
		conn.commit()

def close():
	if((conn  is not None) and (cur is not None)):
		print("Closing the database...")
		cur.close()
		conn.close()

def insert_tweet(tweet):
	if(cur is not None):
		try:
			cur.execute(
	     		 """INSERT INTO \"Tweet\" (t_id, created_at, u_id, text)
	         	VALUES (%s, %s, %s , %s);""",
	     			(tweet.get_tweet_id(), tweet.get_created_at(), 
	     			tweet.get_user_id(), tweet.get_text()))
		except psycopg2.IntegrityError:
			conn.rollback()

def insert_user(user):
	if(cur is not None):
		cur.execute(
     		 """INSERT INTO \"User\" (u_id, description, location, followers_count, friends_count)
         	VALUES (%s, %s, %s , %s, %s);""",
     			(user.get_user_id(), user.get_description(), 
     			user.get_location(), user.get_followers_count(), user.get_friends_count()))

def insert_data(tweet, user):
	if(not(verify_user_existence_in_database(user))):
		insert_user(user)
	insert_tweet(tweet)
	commit_batch_if_threshold()


def verify_user_existence_in_database(user):
	cur.execute("select exists(select 1 from \"User\" where \"u_id\"="+ str(user.get_user_id()) + ");")
	existence = cur.fetchone()[0]
	return existence