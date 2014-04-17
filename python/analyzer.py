__author__ = 'Chong-U Lim, culim@mit.edu'

class Analyzer(object):

	def __init__(self, puzzlescript):
		self.puzzlescript = puzzlescript

	def get_number_of_levels(self):
		return len(self.puzzlescript['levels'].levels)

	def get_number_of_rules(self):
		if ('rules' not in self.puzzlescript):
			return 0
		return len(self.puzzlescript['rules'].rules)

	def get_number_of_winconditions(self):
		return len(self.puzzlescript['winconditions'].winconditions)

	def get_number_of_collisionlayers(self):
		return len(self.puzzlescript['collisionlayers'].collisionlayers)

	def get_number_of_legends(self):
		return len(self.puzzlescript['legend'].legends)

	def get_number_of_objects(self):
		return len(self.puzzlescript['objects'].objects)

	def get_number_of_rule_loops(self):
		return len(self.puzzlescript['rules'].loops)

	def get_number_of_messages(self):
		return len(self.puzzlescript['levels'].messages)

	def get_average_level_width(self):
		widths = [level.width for level in self.puzzlescript['levels'].levels ]
		return sum(widths)/float(len(widths));

	def get_average_level_height(self):
		heights = [level.height for level in self.puzzlescript['levels'].levels ]
		return sum(heights)/float(len(heights))

	def printStats(self, scriptName):
		nObjects =  self.get_number_of_objects()
		nRules =  self.get_number_of_rules()
		nLevels =  self.get_number_of_levels()
		aWidth = self.get_average_level_width()
		aHeight = self.get_average_level_height()
		nWinConditions = self.get_number_of_winconditions()

		res = "%% %% %% ROW %% %% %%\n%s &\n%s &\n%s &\n%s &\n%s &\n%s &\n%s \n\\\\ \\hline" %(scriptName, nObjects,nRules,nLevels,aWidth,aHeight,nWinConditions)

		print res

class LevelAnalyzer(object):
	def __init__(self, level):
		self.level = level

	def get_fragmentation_score(self, level, character):
		'''
		Returns the number of islands in this level that 
		contain the specified character.
		'''

	def get_domination_score(self, level, character):
		'''
		'''

	def get_sparseness_score(self, level, character):
		'''
		'''

	def get_volume_score(self, level, character):
		'''
		'''
