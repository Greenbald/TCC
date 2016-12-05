To use the algorithm, two libraries must be installed in order to work.

  1. psycopg2(Library to connect to an existing postgresql database).
  2. Tweepy(In order to get twitter's tweets and user overall information).
  3. nltk(v3.2.1)
  4. pymonetdb
  
Infos 

  To adapt the algorithm for your needs, one must change the following :
  
  	0. First of all, you must create a database, both in postgresql and monetDB using the respectives .sql files.
  		a) For monetDB : You must download, install and configure an user and password, after that you should try to run the monetdb.sql file.
  		b) For Postgresql : You only need to run the postgresql.sql file in order to create the database.
    1. The file controllers/database_controller.py must be changed to your specific postgresql database.
    2. The normalizer.py has a function called convert_utc_to_brt(utc_time). You must change this function to make it work in your time zone
    3. In data/keywords.data and data/languages.data, make all necessary changes in order to get specific tweets.
    	a) keywords.data : This file contains all keywords that will filter the search for tweets, maximum of 500 keywords(Twitter API restriction).
    	b) languages.data : All tweet languages you want to search.
    4. First you must collect data with tweet_mining.py, and after that, with both DB running, you can run postgre_tweet_to_monetdb.py in order to make the huge table(tweet in row and tokens in column)
