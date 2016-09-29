class Tweet():
    """ A tweet model to save in the database """
    def __init__(self, text, raw_text, tweet_id, 
                source_device, created_time, user_id,
                date, entities, tokens):
        self._text = text
        self._raw_text = raw_text
        self._tweet_id = tweet_id
        self._source_device = source_device
        self._created_time = created_time
        self._user_id = user_id
        self._entities = entities
        self._tokens = tokens
        self._date = date
 
    def get_text(self):
        return self._text

    def get_raw_text(self):
        return self._raw_text

    def get_tweet_id(self):
        return self._tweet_id

    def get_source_device(self):
        return self._source_device

    def get_created_at(self):
        return self._created_time

    def get_user_id(self):
        return self._user_id

    def get_entities(self):
        return self._entities

    def get_tokens(self):
        return self._tokens

    def get_date(self):
        return self._date

    def __repr__(self):
        return "Text : " + str(self._text) + "\n" \
        "Raw_Text : " + str(self._raw_text) + "\n" \
        "Tweet_ID :" + str(self._tweet_id) + "\n" \
        "Source_Device : " + str(self._source_device) + "\n" \
        "Created_Time : " + str(self._created_time) + "\n" \
        "User_ID : " + str(self._user_id) + "\n" \
        "Date : " + str(self._date) + "\n" \
        "Entities : " + str(self._entities) + "\n" \
        "Tokens : " + str(self._tokens) + "\n" \
        "-----------------------------------------------"


class User():
    """ A representation of the user whose tweet was captured """
    
    def __init__(self, user_id, friends_count=0, description=None,
                location=None, followers_count=0):
        self._user_id = user_id
        self._friends_count = friends_count
        self._description = description
        self._location = location
        self._followers_count = followers_count

    
    def get_user_id(self):
        return self._user_id
    
    def get_friends_count(self):
        return self._friends_count

    def get_description(self):
        return self._description
    
    def get_location(self):
        return self._location

    def get_followers_count(self):
        return self._followers_count

    def __repr__(self):
        return "User_Id : " + str(self._user_id) + "\n" \
        "Friends_Count :" + str(self._friends_count) + "\n" \
        "Description : " + str(self._description) + "\n" \
        "Location : " + str(self._location) + "\n" \
        "Followers_Count : " + str(self._followers_count) + "\n" \
        "---------------------------------------------------------"

class Entities():
    """ A representation of the user whose tweet was captured """
    
    def __init__(self, hashtags=[], user_mentions=[], urls=[], symbols=[]):
        self._hashtags = hashtags
        self._user_mentions = user_mentions
        self._urls = urls
        self._symbols = symbols

    
    def get_hashtags(self):
        return self._hashtags
    
    def get_user_mentions(self):
        return self._user_mentions
    
    def get_urls(self):
        return self._urls

    def get_symbols(self):
        return self._symbols

    def __repr__(self):
        return "Hashtags : " + str(self._hashtags) + " ; " \
        "User_Mentions :" + str(self._user_mentions) + " ; " \
        "URLs : " + str(self._urls) + " ; " \
        "Symbols : " + str(self._symbols) + " ; "