from models.model import Tweet, User
from controllers import database_controller
import atexit
from util.normalizer import *

def init_database():
	database_controller.open_database_connection()

def exit_handler(): 
	database_controller.commit()
	database_controller.close()

atexit.register(exit_handler)

def save_data_to_database(data_json):
	tweet = create_tweet_object(data_json)
	user = create_user_object(data_json)

	if(not((tweet is None) or (user is None))):
		database_controller.insert_data(tweet, user)

def create_tweet_object(data_json):
	""" Creates an object of type Tweet with the
		data in the data_json arg """

	user_json = data_json.get("user", None)

	if(user_json is not None):
		if(data_json.get("id_str", None) is None):
			return None

		source_device = normalize_source_device(str(data_json.get("source")))
		
		t = normalize_time(data_json.get("created_at"))

		tweet = Tweet(data_json.get("text"), data_json.get("id_str"), 
					  source_device, t, user_json.get("id"))

		return tweet

	return None

def create_user_object(data_json):
	""" Creates an object of type User with the
		data in the user_json arg """
	user_json = data_json.get("user", None)
	if(user_json is not None):

		user = User(user_json.get("id"), user_json.get("friends_count", 0), 
			user_json.get("description", None), user_json.get("location", None), 
			user_json.get("followers_count", 0))
		return user
	return None