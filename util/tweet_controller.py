from model.model import Tweet, User

def get_data_objects(data_json):
	""" This function makes two objects regarding the argument :
		Obj 1 : Tweet type, contain information about the tweet itself
		Obj 2 : User type, contain information about the User itself """
	tweet = create_tweet_object(data_json)
	user = create_user_object(data_json)
	print(user)

def create_tweet_object(data_json):
	""" Creates an object of type Tweet with the
		data in the data_json arg """

	user_json = data_json.get("user", None)

	if(user_json is not None):

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

		tweet = Tweet(data_json.get("text"), data_json.get("id_str"), 
					  source_device, data_json.get("created_at"), user_json.get("id"))
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