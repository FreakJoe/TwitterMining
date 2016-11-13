import configparser

class Config():
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read("config.ini")

		self.values = {}
		self.read_values()

	def read_values(self):
		for section in self.config.sections():
			for option in self.config.options(section):
				self.values[option] = self.config.get(section, option)

	def get(self, key):
		return self.values[key]

config = Config()