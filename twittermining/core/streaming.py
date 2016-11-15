import re
import tweepy
from .config import config
from .database import database

CONSUMER_KEY = config.get('consumer_key')
CONSUMER_SECRET = config.get('consumer_secret')
ACCESS_TOKEN = config.get('access_token')
ACESS_TOKEN_SECRET = config.get('access_token_secret')

class StreamListener(tweepy.StreamListener):
	track = ''
	
	def on_status(self, status):
		if status.lang != 'en':
			return
			
		user = self.fix_encoding(status.user.name)
		text = self.fix_encoding(status.text)
		hashtags = self.get_hashtags(text)
		search_topic = self.track
		database.add_tweet(user, text, hashtags, search_topic)
		print('\n---------\n', user, '\n----------\n', text, '\n---------\n')

	def fix_encoding(self, text):
		text = text.encode('ascii', 'ignore')
		text = text.decode('ascii')
		return text

	def get_hashtags(self, text):
		hashtags = re.findall("#\S*", text)
		return hashtags

def stream_into_db(track='twitter'):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	stream_listener = StreamListener()
	# To allow categorizing tweets in the database
	stream_listener.track = track
	stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
	stream.filter(track=[track])