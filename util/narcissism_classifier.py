import codecs
import unicodedata

with codecs.open('data/classifier_words.data', encoding='utf-8', mode='r') as f:
	swear_words = [str(x).replace("\n", "").strip().lower() for x in f]

def classify_tweet(tokens):
	for t in tokens:
		g = t.strip().lower()
		for sw in swear_words:
			if sw == g:
				return True

	return False