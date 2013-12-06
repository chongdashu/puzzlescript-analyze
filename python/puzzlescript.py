import re

class Script(object):


	def __init__(self, txt):
		self.txt = txt

		self.title = None
		self.author = None
		self.homepage = None

		if txt:
			self.parse(txt)

	def parse(self, txt):
		 lines = txt.split("\n")
		 for line in lines:
		 	self.parse_line(line)

	def parse_line(self,txt):
		match = None

		# Title
		match = re.match("title ([a-z A-Z]+)", txt)
		if not self.title and match:
			self.title = match.group(1)

		# Author
		match = re.match("author ([a-z A-Z]+)", txt)
		if not self.author and match:
			self.author = match.group(1)

		# Homepage
		match = re.match("homepage ([a-z A-Z.\/:]+)", txt)
		if not self.homepage and match:
			self.homepage = match.group(1)
