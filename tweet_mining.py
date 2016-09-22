from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from controllers.tweet_controller import *
import json
import codecs
import sys
import signal

DEBUG = "-debug"


# RELATED TO SYS ARGUMENTS
if(len(sys.argv) > 1):
    if(sys.argv[1].lower() != DEBUG):
        signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))
else:
    signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))
# END 

consumer_key = "6ZvBQkiTM2rX2svhAlMgg3Ekm"
consumer_secret = "Xxyg43oq6JHoGrWS0zFXkUysscDuTk1FYIABsrbNpputlouJED"
access_token = "2876597908-XuwL9VoPI6jw5ErlyqnlCiwGXWyzG81SDAf1gE2"
access_token_secret = "pZc6J6mLPi5DIGUDMp5p2l1HEUDtuwZLinstQ00YMQiwS"

# RELATED TO FILE ACCESS TO GET ALL KEYWORDS AND LANGUAGES OF TWEETS
def get_keywords():

    keywords = []
    with codecs.open('data/keywords.data', encoding='utf-8', mode='r') as f:
        for line in f:
            l = line.replace("\n", "")
            l = str(l.replace("\r", ""))
            keywords.append(l)
    return keywords

def get_languages():
    languages = []
    with codecs.open('data/languages.data', encoding='utf-8', mode='r') as f:
        for line in f:
            l = line.replace("\n", "")
            l = str(l.replace("\r", ""))
            languages.append(l)
    return languages
# END

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        json_obj = json.loads(data)
        save_data_to_database(json_obj)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    init_database()

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    keywords = get_keywords()
    lang = get_languages()  

    stream = Stream(auth, l)
    stream.filter(languages=lang, track=keywords)