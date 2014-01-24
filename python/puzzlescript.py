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

 
	def __repr__(self):
		return "sections: %s" %(self.sections.keys())


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

	def set(self, key, value):
		self.tokens[key] = value

	def get(self, key):
		return self.tokens.get(key)

	def type(self):
		return self.type

	def __repr__(self):
		return "%s{%s}" %(self.type.upper(), self.tokens.keys())

	def parse_line(self,line):
		match = None

		# Title
		match = re.match("([a-z]+) +(.+)", line)
		if match:
			token = match.group(1)
			value = match.group(2)

			self.set(token, value)

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

class LegendSection(Section):

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










