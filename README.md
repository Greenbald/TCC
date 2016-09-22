To use the algorithm, two libraries must be installed in order to make it work.

  1. psycopg2(Library to connect to an existing postgresql database).
  2. Tweepy(In order to get twitter's tweets and user overall information).
  
Infos 

  To adapt the algorithm for your needs, one must change the following :
  
    1. The file controllers/database_controller.py must be changed to your specific postgresql database.
    2. The normalizer.py has a function called convert_utc_to_brt(utc_time). You must change this function to make it work in your time zone
    3. In data/keywords.data and data/languages.data, make all necessary changes in order to get specific tweets.
    	a) keywords.data : This file contains all keywords that will filter the search for tweets, maximum of 500 keywords(Twitter API restriction).
    	b) languages.data : All tweet languages you want to search.
    4. The algorithm commits the data to database every time it reaches a threshold of 100. So, every 100 tweets, the algorithm will commit the data changes to database. This is done in database_controller.py
