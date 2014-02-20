__author__ = 'Chong-U Lim, culim@mit.edu'

class Analyzer(object):

	def __init__(self, puzzlescript):
		self.puzzlescript = puzzlescript

	def get_number_of_levels(self):
		return len(self.puzzlescript['levels'].levels)

	def get_number_of_rules(self):
		return len(self.puzzlescript['rules'].rules)

	def get_number_of_winconditions(self):
		return len(self.puzzlescript['winconditions'].conditions)

	def get_number_of_collisionlayers(self):
		return len(self.puzzlescript['collisionlayers'].collisionlayers)

	def get_number_of_legends(self):
		len(self.puzzlescript['legend'].tokens)

	def get_number_of_objects(self):
		len(self.puzzlescript['objects'].tokens)