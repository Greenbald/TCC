from models.model import Entities
import re
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