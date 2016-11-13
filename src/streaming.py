import tweepy
from config import config

auth = tweepy.OAuthHandler(config.get('consumer_key'), config.get('consumer_secret'))
auth.set_access_token(config.get('access_token'), config.get('access_token_secret'))
api = tweepy.API(auth)