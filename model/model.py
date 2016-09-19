
class Tweet(Object):
    """ A tweet model to save in the database """
    def __init__(self, text=None, tweet_id=None, source_device=None):
        self._text = text
        self._tweet_id = tweet_id
        self._source_device = source_device

    @property
    def get_text(self):
        return _text

    @property
    def get_tweet_id(self):
        return _tweet_id

    @property
    def get_source_device(self):
        return _source_device

class User(Object):
    """ A representation of the user whose tweet was captured """
    
    def __init__(self, user_id=None, friends_count=None, description=None,
        location=None, followers_count=None):
        self._user_id = user_id
        self._friends_count = friends_count
        self._description = description
        self._location = location
        self._followers_count = followers_count

    @property
    def get_user_id(self):
        return _user_id

    @property
    def get_friends_count(self):
        return _friends_count

    @property
    def get_description(self):
        return _description

    @property
    def get_location(self):
        return _location

    @property
    def get_followers_count(self):
        return _followers_count

