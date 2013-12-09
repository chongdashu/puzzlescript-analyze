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
		return "sections: %s" %(self.sections)


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
		return "tokens: %s" %(self.tokens.keys())

	@staticmethod
	def create(type_):
		sectionType = type_.lower()

		if sectionType == Section.TYPE_PRELUDE:
			return PreludeSection(sectionType)

		return None

	@staticmethod
	def is_section(name):
		return name.lower() in Section.TYPES



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







