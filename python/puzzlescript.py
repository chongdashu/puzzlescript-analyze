import re

class Script(object):

	def __init__(self, txt):
		self.sections = {}
		self.txt = txt

		if (self.txt):
			self.parse(txt)

	def parse(self, txt):
			
		section = Section.create(Section.TYPE_PRELUDE)
		
		lines = txt.split("\n")
		for line in lines:
			section.parse_line(line)

		self.sections[Section.TYPE_PRELUDE] = section

	def section(self, name):
		return self.sections.get(name)




	def __repr__(self):
		return "sections: %s" %(self.sections)


class Section(object):

	TYPE_PRELUDE = "Prelude"
	TYPE_OBJECTS = "Objects"
	TYPE_LEGEND = "Legend"
	TYPE_SOUNDS = "Sounds"
	TYPE_COLLISIONLAYERS = "CollisionLayers"
	TYPE_RULES = "Rules"
	TYPE_WINCONDITIONS = "WinConditions"
	TYPE_LEVELS = "Levels"

	def __init__(self):
		self.tokens = {}

	def set(self, key, value):
		self.tokens[key] = value

	def get(self, key):
		return self.tokens.get(key)

	def __repr__(self):
		return "tokens: %s" %(self.tokens.keys())

	@staticmethod
	def create(type_):
		if type_ == Section.TYPE_PRELUDE:
			return PreludeSection()

		return None



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

	def __init__(self):
		Section.__init__(self)

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





