import requests

def call_genderize(name):
	"""Makes a call to the genderize.io API	to determine the probable 
	gender connected to a first name or list of first names as name"""
	request = requests.get('https://api.genderize.io/', params={'name': name})
	return request.json()

def first_name_gender(name):
	"""Returns the probable gender(s) of a (list of) name(s)"""
	# Ensure the API is given valid input
	if (type(name) != str and type(name) != list) or (type(name) == list and len(name) > 10):
		return None

	gender = {}
	response = call_genderize(name)
	if type(name) == str:
		response = [response]

	# Turn a list of dicts into a dict merely assigning each name (key) a gender (value)
	for n in response:
		gender[n['name']] = n['gender']

	return gender