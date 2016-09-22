To use the algorithm, two libraries must be installed in order to make it work.

  1. psycopg2(Library to connect to a existing postgresql database).
  2. Tweepy(In order to get twitter's tweets and user overall information).
  
Infos 

  To adapt the algorithm for your needs, one must change the following :
  
    1. The file controllers/database_controller.py must be changed to your specific postgresql database.
    2. The normalizer.py has a function called convert_utc_to_brt(utc_time). You must change this function to make it work in your time zone
    3. In tweet_mining.py, there's a function call (stream.filter(...)), change those words in the parameter to get more specific tweets.
