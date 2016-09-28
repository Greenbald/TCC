from models.model import Tweet, User, Entities
from controllers import database_controller
import atexit
from util.factory import *

def init_database():
	database_controller.open_database_connection()

def exit_handler(): 
	database_controller.close()

atexit.register(exit_handler)

def save_data_to_database(data_json):
	entities = create_entities_object(data_json)
	tweet = create_tweet_object(data_json, entities)
	user = create_user_object(data_json)

	if(not((tweet is None) or (user is None))):
		database_controller.insert_data(tweet, user)