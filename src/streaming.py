import re
import tweepy
from config import config
from database import database

CONSUMER_KEY = config.get('consumer_key')
CONSUMER_SECRET = config.get('consumer_secret')
ACCESS_TOKEN = config.get('access_token')
ACESS_TOKEN_SECRET = config.get('access_token_secret')

class StreamListener(tweepy.StreamListener):
	def on_status(self, status):
		user = self.fix_encoding(status.user.name)
		text = self.fix_encoding(status.text)
		hashtags = self.get_hashtags(text)
		database.add_tweet(user, text, hashtags)
		print('\n---------\n', user, '\n----------\n', text, '\n---------\n')

	def fix_encoding(self, text):
		text = text.encode('ascii', 'ignore')
		text = text.decode('ascii')
		return text

	def get_hashtags(self, text):
		hashtags = re.findall("#\S*", text)
		return hashtags

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)
api = tweepy.API(auth)

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=['#Election2016'])