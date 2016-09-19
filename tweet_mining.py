from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from util.tweet_controller import decode

consumer_key = "6ZvBQkiTM2rX2svhAlMgg3Ekm"
consumer_secret = "Xxyg43oq6JHoGrWS0zFXkUysscDuTk1FYIABsrbNpputlouJED"
access_token = "2876597908-XuwL9VoPI6jw5ErlyqnlCiwGXWyzG81SDAf1gE2"
access_token_secret = "pZc6J6mLPi5DIGUDMp5p2l1HEUDtuwZLinstQ00YMQiwS"



class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print(data)
        decoded_data = decode(data)
        print(decoded_data.get('gg') )
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(languages=['pt'], track=["e", u"é", "eu", "ele", "esse", "para", "pra", ".", "mais", "mas", u"não", "nao", "n"])