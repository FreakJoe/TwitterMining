from ..core.database import database
from ..core.language.names import extract_first_name, first_name_gender

def copy_tweets_to_analyse():
	"""Copies all tweets into a new database table for manipulation"""
	for tweet in database.get_tweets():
		user = tweet.user
		text = tweet.text
		hashtags = tweet.hashtags
		search_topic = tweet.search_topic

		database.add_tweet_analysis(user, text, hashtags, str(None), search_topic)

def all_tweets_gender():
	for tweet in database.get_tweets_analysis():
		user = tweet.user
		first_name = extract_first_name(user)

		if first_name: 
			gender = first_name_gender(first_name)[first_name]

		else: 
			gender = str(None)

		tweet.gender = gender
		database.commit()

		print('--------')
		print(tweet.user)
		print(first_name)
		print(gender)
		print('--------')