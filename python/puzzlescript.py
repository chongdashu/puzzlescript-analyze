__author__ = 'Chong-U Lim, culim@mit.edu'

import re

class Script(object):

	def __init__(self, txt):
		self.sections = {}
		self.txt = txt

		if (self.txt):
			self.parse(txt)

	def parse(self, txt):
			
		section = Section.create(Section.TYPE_PRELUDE)
		self.add_section(section)
		
		lines = txt.split("\n")
		for line in lines:
			if Section.is_section(line):
				# Check if the line has a keyword for the start
				# of a new section.
				print 'Parsing section: %s' %(line)
				section = self.create_section(line)
				
			if section:
				section.parse_line(line)

	def add_section(self, section):
		self.sections[section.type] = section

	def section(self, name):
		return self.sections.get(name)

	def create_section(self, name):
		
		section = Section.create(name)
		if section:
			self.add_section(section)

		return section

	def __getitem__(self, index):
		return self.sections[index.lower()]
 
	def __repr__(self):
		return "Script(%s)" %(self.sections.keys())

# ------- Elements ------- #
class PSMessage(object):
	def __init__(self, text, last_level_index_=0):
		self.last_level_index = last_level_index_
		self.text = text

	def __repr__(self):
		return "PSMessage(%s,%s)" %(self.last_level_index, self.text)
				
class PSLevel(object):

	def __init__(self):
		self.definition = []
		self.width = 0
		self.height = 0

	def __repr__(self):
		return "PSLevel[%sx%s](%s)" %(self.width,self.height,self.definition)

	def parse_line(self, line):
		self.definition.append(line)
		self.width = len(line)
		self.height += 1

class PSObject(object):

	def __init__(self, line):
		self.definition = []

		self.declaration = line
		self.declaration_tokens = line.split(" ")
		
		self.name = self.declaration_tokens[0]
		if len(self.declaration_tokens) > 1:
			self.legend = self.declaration_tokens[1]

	def __repr__(self):
		return "PSOBject(%s)" %(self.declaration)

	def parse_line(self, line):
		self.definition.append(line)

class PSRule(object):

	def __init__(self, line):
		match = re.match("((.)+)\s*->\s*((.)+)", line)
		if match:
			self.lhs = match.group(1)
			self.rhs = match.group(3)

	def __repr__(self):
		return "PSRule(%s)" %str(self)

	def __str__(self):
		return "%s -> %s" %(self.lhs, self.rhs)

class PSWinCondition(object):

	OPERATOR_NO = "no"
	OPERATOR_ALL = "all"
	OPERATOR_SOME = "some"

	def __init__(self, line):
		self.text = line.strip()
		self.args = []
		self.condition = ""

		match = re.match("((.)+) ((.)+)\son\s((.)+)", self.text)
		if match:
			self.condition = match.group(1)
			self.args.append(match.group(3))
			self.args.append(match.group(5))
		else:
			match = re.match("((.)+)\s((.)+)", self.text)
			if match:
				self.condition = match.group(1)
				self.args.append(match.group(3))

	def __repr__(self):
		return "PSWinCondition(%s)" %str(self)

	def __str__(self):
		string = "[%s] [%s]" %(self.condition, self.args[0])
		if len(self.args) > 1:
			string += " on [%s]" %(self.args[1])

		return string


class PSCollisionLayer(object):

	def __init__(self, line):
		self.objects = line.strip().split(',')

	def __repr__(self):
		return "PSCollisionLayer(%s)" %str(self)

	def __str__(self):
		return str(self.objects)




# ------- Sections------- #
class Section(object):

	TYPE_PRELUDE = "prelude"
	TYPE_OBJECTS = "objects"
	TYPE_LEGEND = "legend"
	TYPE_SOUNDS = "sounds"
	TYPE_COLLISIONLAYERS = "collisionlayers"
	TYPE_RULES = "rules"
	TYPE_WINCONDITIONS = "winconditions"
	TYPE_LEVELS = "levels"

	TYPES = [
		TYPE_PRELUDE,
		TYPE_OBJECTS,
		TYPE_LEGEND,
		TYPE_SOUNDS,
		TYPE_COLLISIONLAYERS,
		TYPE_RULES,
		TYPE_WINCONDITIONS,
		TYPE_LEVELS
	]

	def __init__(self, type_):
		self.tokens = {}
		self.type = type_
		self.is_parsing_comment = False

	def set(self, key, value):
		self.tokens[key] = value

	def get(self, key):
		return self.tokens.get(key)

	def type(self):
		return self.type

	def __repr__(self):
		return "%s{%s}" %(self.type.upper(), self.tokens.keys())

	def parse_line(self,line):
		parsed_line = False

		line = line.strip()
		if self.is_parsing_comment:
			match = re.match("(.)*\)", line)
			if match:
				self.is_parsing_comment = False 
				print "\tEnding comment: %s" %line
			return True

		match = re.match("\((.)+", line)

		if match:

			if not match.group(1) == ")":
				self.is_parsing_comment = True
				print "\tStarting comment: %s" %line
			else:
				print "\tSkipping comment: %s" %line
			parsed_line = True

		return parsed_line
		

	# Static methods
	################
	@staticmethod
	def create(type_):
		sectionType = type_.lower()

		if sectionType == Section.TYPE_PRELUDE:
			return PreludeSection(sectionType)
		elif sectionType == Section.TYPE_OBJECTS:
			return ObjectsSection(sectionType)
		elif sectionType == Section.TYPE_LEGEND:
			return LegendSection(sectionType)
		elif sectionType == Section.TYPE_LEVELS:
			return LevelsSection(sectionType)
		elif sectionType == Section.TYPE_RULES:
			return RulesSection(sectionType)
		elif sectionType == Section.TYPE_WINCONDITIONS:
			return WinConditionsSection(sectionType)
		elif sectionType == Section.TYPE_COLLISIONLAYERS:
			return CollisionLayersSection(sectionType)
		elif sectionType == Section.TYPE_SOUNDS:
			return SoundsSection(sectionType)
		else:
			return Section(sectionType)


	@staticmethod
	def is_section(name):
		return name.lower() in Section.TYPES

	@staticmethod
	def is_comment(line):
		return re.match("(=)+",line) is not None

	@staticmethod
	def is_keyline(line):
		return Section.is_section(line) or Section.is_comment(line)

class SoundsSection(Section):
	def __init__(self, type_):
		Section.__init__(self,type_)
		self.sounds = []


	def parse_line (self, line):
		if (Section.parse_line(self, line)):
			return
		if line.strip() and not Section.is_keyline(line):
			self.sounds.append(line.strip())



class CollisionLayersSection(Section):

	def __init__(self, type_):
		Section.__init__(self,type_)
		self.collisionlayers = []

	def parse_line (self, line):
		if Section.parse_line(self,line):
			return
		if line.strip() and not Section.is_keyline(line):
			layer = PSCollisionLayer(line)
			self.collisionlayers.append(layer)


class WinConditionsSection(Section):

	def __init__(self, type_):
		Section.__init__(self,type_)
		self.winconditions = []

	def parse_line(self, line):
		parsed_line = Section.parse_line(self,line)
		if parsed_line :
			return
		if line.strip() and not Section.is_keyline(line):
			print '\tParsing Win Condition: %s' %(line.strip())
			wincondition = PSWinCondition(line.strip())
			self.winconditions.append(wincondition)


class RulesSection(Section):
	def __init__(self, type_):
		Section.__init__(self,type_)
		self.rules = []
		self.loops = []
		self.current_loop = None

	def parse_line(self, line):
		parsed_line = Section.parse_line(self,line)
		if parsed_line:
			return

		if line.strip() and line.strip().lower() == "startloop":
			self.current_loop = [];

		elif line.strip() and line.strip().lower() == "endloop":
			self.loops.append(self.current_loop)
			self.current_loop = None

		elif line.strip() and not Section.is_keyline(line):
			print '\tParsing Rule: %s' %(line.strip())
			rule = PSRule(line.strip())

			self.rules.append(rule)
			self.tokens[rule.lhs] = rule

			if self.current_loop is not None:
				self.current_loop.append(rule)

class LevelsSection(Section):
	def __init__(self, type_):
		Section.__init__(self,type_)

		# Indicates if already parsed an object declaration
		# and that we are now currently parsing the definition
		# of the object.
		self.isParsingLevel = False
		self.levels = []
		self.messages = []
		self.current_level = None

	def parse_line(self, line):
		if self.isParsingLevel:
			
			if line.strip():
				# Case (1): Non-empty line means that we are still parsing the
				#			level definition.	
				self.current_level.parse_line(line)
			else:
				# Case (2): Empty line means that we are done. 
				self.isParsingLevel = False
				self.tokens[len(self.levels)] = self.current_level
				self.levels.append(self.current_level)
		else:
			if line.strip() and not Section.is_keyline(line):
				# Case (3): Non-empty line. Need to check if start of 
				#			a level, or a message.
				match = re.match("MESSAGE ((.)+)", line.strip(), re.IGNORECASE)
				if match:
					# Case (3a): A message.
					print '\tCreating new message: %s' %(line)
					text = match.group(1)
					message = PSMessage(text, len(self.levels))
					self.messages.append(message)
				else:
					# Case (3b): A level definition start.
					print '\tCreating new level: %s' %(line)
					self.current_level = PSLevel()
					self.current_level.parse_line(line)
					self.isParsingLevel = True




class LegendSection(Section):

	def __init__(self, type_):
		Section.__init__(self,type_)
		self.legends = self.tokens

	def parse_line(self, line):
		if line.strip() and not Section.is_keyline(line):
			print '\tParsing Legend: %s' %(line)
			line_tokens = line.split("=")
			key = line_tokens[0].strip()
			if re.match("[a-zA-Z]+ and [a-zA-Z]+", line_tokens[1].strip()):
				val = tuple(x.strip() for x in line_tokens[1].strip().split("and"))
			else:
				val = tuple(x.strip() for x in line_tokens[1].strip().split("or"))
			self.tokens[key] = val


class ObjectsSection(Section):

	def __init__(self, type_):
		Section.__init__(self,type_)
		# Indicates if already parsed an object declaration
		# and that we are now currently parsing the definition
		# of the object.
		self.isParsingDefinition = False
		self.objects = self.tokens

	def parse_line(self, line):

		if self.isParsingDefinition:
			
			if line.strip():
				# Case (1): Non-empty line means that we are still parsing the
				#			objects definition.	
				self.current_object.parse_line(line)

			else:
				# Case (2): Empty line means that the definition is ending.
				self.isParsingDefinition = False
				self.tokens[self.current_object.name] = self.current_object
			
		else:
			
			if line.strip() and not Section.is_keyline(line):
				print '\tCreating new object: %s' %(line)
				self.current_object = PSObject(line)
				self.isParsingDefinition = True	

class PreludeSection(Section):

	TOKEN_AUTHOR = "author"
	TOKEN_COLOR_PALETTE = "color_palette"
	TOKEN_AGAIN_INTERVAL = "again_interval"
	TOKEN_BACKGROUND_COLOR = "debug"
	TOKEN_FLICKSCREEN = "flickscreen"
	TOKEN_HOMEPAGE = "homepage"
	TOKEN_KEY_REPEAT_INTERVAL = "key_repeat_interval"
	TOKEN_NOACTION = "noaction"
	TOKEN_NORESTART = "norestart"
	TOKEN_REQUIRE_PLAYER_MOMENT = "require_player_moment"
	TOKEN_RUN_RULES_ON_LEVEL_START = "run_rules_on_level_start"
	TOKEN_SCANLINE = "scanline"
	TOKEN_TEXT_COLOR = "text_color"
	TOKEN_TITLE = "title"
	TOKEN_VERBOSE_LOGGING = "verbose_logging"
	TOKEN_YOUTUBE = "youtube"
	TOKEN_ZOOMSCREEN = "zoomscreen"

	def __init__(self, type_):
		Section.__init__(self, type_)

		self.title = None
		self.author = None
		self.homepage = None

	def parse_line(self,line):
		match = None

		# Title
		match = re.match("([a-z]+) +(.+)", line)
		if match:
			token = match.group(1)
			value = match.group(2)

			self.set(token, value)










