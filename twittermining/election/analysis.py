from ..core.database import database
from ..core.language.names import extract_first_name, first_name_gender

def all_tweets_gender():
	for tweet in database.get_tweets():
		name = tweet.user
		first_name = extract_first_name(name)
		if first_name: 
			gender = first_name_gender(first_name)[first_name]

		else: 
			gender = None

		print('--------')
		print(tweet.user)
		print(first_name)
		print(gender)
		print('--------')