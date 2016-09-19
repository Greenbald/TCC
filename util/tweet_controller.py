import json
from model.model import Tweet, User

def decode(s):
	return json.loads(s)

def get_tweet_model(*args):
	""" Param 0 : Must be a json containing the twitter's tweet json format
		Param 1...N : Must be an available attribute in the json file """
	#TODO

