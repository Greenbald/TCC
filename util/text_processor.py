from models.model import *
import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import codecs
import string

with codecs.open('data/stopwords.data', encoding='utf-8', mode='r') as f:
	stop_words = [str(x).replace("\n", "").strip().lower() for x in f]

def remove_entities(text, entities):
	new_text = _replace_entities(entities.get_hashtags(), text)
	new_text = _replace_entities(entities.get_symbols(), new_text)
	new_text = _replace_entities(entities.get_user_mentions(), new_text)
	new_text = _replace_entities(entities.get_urls(), new_text)
	return new_text

def _replace_entities(entity, text):
	new_text = text
	for i in entity:
		pattern = re.compile(i, re.IGNORECASE)
		new_text = pattern.sub("", new_text)
	return new_text

def tokenize_tweet(text):
	global stop_words
	text = text.lower()
	tokenizer = TweetTokenizer()
	tokens = tokenizer.tokenize(text)
	tokens = [tok for tok in tokens if tok not in stop_words and not tok.isdigit()]
	return tokens