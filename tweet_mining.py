from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import Stream
from controllers.tweet_controller import *
import json
import codecs
import sys
import signal
from util import twitter_oauth
from http.client import IncompleteRead

DEBUG = "-debug"

# RELATED TO SYS ARGUMENTS
if(len(sys.argv) > 1):
    if(sys.argv[1].lower() != DEBUG):
        signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))
else:
    signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))
# END 

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
    auth = twitter_oauth.get_twitter_auth()

    keywords = get_keywords()
    lang = get_languages()  
    while True:
        try:
            stream = Stream(auth, l)
            stream.filter(languages=lang, track=keywords)
        except IncompleteRead:
            continue