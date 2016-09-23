import time


def normalize_source_device(source):

	source_device = source

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

	return source_device

def convert_utc_to_brt(utc_time):
	""" UTC time is 3 hours ahead of brazil 
		it does not consider the summer time """
	i = 2
	if(":" in utc_time[:i]):
		i -= 1
	h = int(utc_time[:i]) - 3
	r = utc_time[i:]
	if(h < 0):
		h = h + 24
	return str(h) + r


def normalize_time(t):
	""" This function is necessary because the time zone provided
		by the twitter is UTC, so we need to convert to BRT(-3h). 
		of course this is not necessarily true, because exists 
		summer time. But... It will work for now. =D"""

	new_t = time.strftime('%H:%M:%S', time.strptime(t,'%a %b %d %H:%M:%S +0000 %Y'))

	new_t = convert_utc_to_brt(new_t)

	h = int(new_t.split(":")[0])
	if(h >= 6 and h < 12):
		return "Manha"
	elif(h >= 12 and h < 18):
		return "Tarde"
	elif(h >= 18 and h <= 23):
		return "Noite"
	elif(h >= 0 and h < 6):
		return "Madrugada"