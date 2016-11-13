import configparser

class Config():
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read("..\config.ini")

		self.values = {}
		self.read_values()

	def read_values(self):
		if 'db' in self.config.sections():
			for option in self.config.options('db'):
				self.values[option] = self.config.get('db', option)

		else:
			self.values = None

	def url(self):
		return self.values['url']