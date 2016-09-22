from model.model import Tweet, User
from util import database_controller
import atexit
import time

def init_database():
	database_controller.open_database_connection()

def exit_handler():
	database_controller.commit()
	database_controller.close()

atexit.register(exit_handler)

def get_data_objects(data_json):
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

		source_device = str(data_json.get("source"))

		if("android" in source_device.lower()):
			source_device = "Android"
		elif("iphone" in source_device.lower()):
			source_device = "Iphone"
		elif("ipad" in source_device.lower()):
			source_device = "Ipad"
		elif("facebook" in source_device.lower()):
			source_device = "Facebook"
		elif("instagram" in source_device.lower()):
			source_device = "Instagram"
		else:
			source_device = "Web"

		t = time.strftime('%H:%M:%S', time.strptime(data_json.get("created_at"),'%a %b %d %H:%M:%S +0000 %Y'))

		t = convert_utc_to_brt(t)
		
		t = normalize_time(t)

		tweet = Tweet(data_json.get("text"), data_json.get("id_str"), 
					  source_device, t, user_json.get("id"))

		return tweet

	return None

def utc_to_local(utc_dt):
	 return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

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

def convert_utc_to_brt(utc_time):
	""" UTC time is ahead in 3 hours of brazil 
		it does not consider the summer time """
	h = int(utc_time[:2]) - 3
	if(h < 0):
		h = h + 24
	return str(h) + utc_time[2:]

def normalize_time(time):
	h = int(time[:2])
	if(h >= 6 and h < 12):
		return "Manha"
	elif(h >= 12 and h < 18):
		return "Tarde"
	elif(h >= 18 and h <= 23):
		return "Noite"
	elif(h >= 0 and h < 6):
		return "Madrugada"