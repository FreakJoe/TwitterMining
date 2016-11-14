import requests
import re

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

def extract_first_name(name):
	"""If a string contains a name, returns that name."""
	if not is_name(name):
		return None

	else:
		return re.match("\w{1,20}(?=\s{1}\w{1,30})", name).group(0)

def is_name(name):
	"""Checks if a string contains a name."""
	return re.match("\w{1,20}(?=\s{1}\w{1,30})", name)