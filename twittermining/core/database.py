from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .tweet import Tweet, Base
from .config import config

class Database():
	def __init__(self):
		self.config = config
		self.base = Base
		self.engine = create_engine('{}'.format(self.config.get('url')))
		self.base.metadata.create_all(self.engine)

		db_session = sessionmaker(bind=self.engine)
		self.session = db_session()

	def add_tweet(self, user, tweet, hashtags, search_topic):
		new_tweet = Tweet(user=user, text=tweet, hashtags=hashtags, search_topic=search_topic)
		self.session.add(new_tweet)
		self.session.commit()

	def get_tweets(self, limit=None):
		if limit:
			return

		return self.session.query(Tweet).all()

database = Database()