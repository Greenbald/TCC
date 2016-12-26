import codecs
import unicodedata

with codecs.open('data/swear_words.data', encoding='utf-8', mode='r') as f:
	swear_words = [str(x).replace("\n", "").strip().lower() for x in f]


def strip_accents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def classify_tweet(tokens):
	for t in tokens:
		g = strip_accents(t).strip().lower()
		for sw in swear_words:
			if sw in g:
				return True

	return False