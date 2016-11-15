from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .tweet import Tweet, TweetAnalysis, Base
from .config import config

class Database():
	def __init__(self):
		self.config = config
		self.base = Base
		self.engine = create_engine('{}'.format(self.config.get('url')))
		self.base.metadata.create_all(self.engine)

		db_session = sessionmaker(bind=self.engine)
		self.session = db_session()

	def add(self, object):
		self.session.add(object)
		self.commit()

	def add_tweet(self, user, tweet, hashtags, search_topic):
		new_tweet = Tweet(user=user, text=tweet, hashtags=hashtags, search_topic=search_topic)
		self.add(new_tweet)

	def add_tweet_analysis(self, user, tweet, hashtags, gender, search_topic):
		new_tweet_analysis = TweetAnalysis(user=user, text=tweet, hashtags=hashtags, gender=gender,  search_topic=search_topic)
		self.add(new_tweet_analysis)

	def get_tweets(self, limit=None):
		if limit:
			return

		return self.session.query(Tweet).all()

	def get_tweets_analysis(self, limit=None):
		if limit:
			return

		return self.session.query(TweetAnalysis).all()

	def commit(self):
		self.session.commit()

database = Database()