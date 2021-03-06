PuzzleScript Analyze
====================

An experimental research project looking into some interesting characteristics of [PuzzleScript](http://www.puzzlescript.net) games.

This is some pretty early stage work, so there isn't anything particularly interesting at this point. Currently, the first couple of steps involve getting a [Python](http://www.python.org) script to parse the PuzzleScript files. 

Requirements
------------
For most any Python libraries, I make use of virtualenv and pip as they help keep my Python environments separate per project I use. 

* Beautiful Soup 4 (beautifulsoup4) 
http://www.crummy.com/software/BeautifulSoup/

Quick-Start
-----------
The easiest way to get started is to just load a puzzlescript file. Assuming you have the PuzzleScript script stored as game.txt (here we are using the Lime Rick example):

> txt = open("../scripts/game.txt").read()
> script = PuzzleScript(txt)

You can get the various sections in the following way:

> script['objects']
OBJECTS{['PlayerHead4', 'Apple', 'PlayerBodyV', 'PlayerHead1', 'PlayerHead2', 'PlayerHead3', 'Crate', 'Wall', 'Exit', 'PlayerBodyH', 'Background']}

> script['rules']
RULES{['UP [ UP PlayerHead4 ]', 'Horizontal [ > Player | Crate | No Obstacle ]', 'DOWN [ Player | No Obstacle ]', 'UP [ UP PlayerHead3 | No Obstacle ]', '[ > Player ]', 'DOWN [ Crate | No Obstacle ]', 'Horizontal [ > Player | No Obstacle ]', 'UP [ UP PlayerHead1 | No Obstacle ]', 'UP [ UP PlayerHead2 | No Obstacle ]', '[ Player Apple ]', '[ Player Apple ] [ PlayerBody ]']}

Credits & Thanks
----------------
- Stephen Lavelle (@increpare) for creating PuzzleScript.
- Toomi Tuovinen (www.kissmaj7.com) for porting 'Lime Rick' to PuzzleScript.
- Michael Cook (@mtrc) for his work on fitness function of game components.

To-dos
------
- [ ] Local copies of default PuzzleScript demo scripts.
- [ ] Rule mutations with constraints.
- [ ] Debug Logger	
- [ ] Stats generation
	- [X] Number of levels.
	- [X] Number of rules.
	- [X] Number of win conditions.
	- [X] Number of collision layers.
	- [X] Number of objects.
	- [X] Number of legends.
	- [X] Number of rule loops.
	- [X] Number of messages.
	- [ ] Size of levels (width/height).
	- [ ] Number of colors used for objects.
	- [ ] Size of objects.
	- [ ] Rating (where possible)
- [ ] Level Analysis
	- [X] Flood-fill
	- [ ] Fragmentation (i.e., number of islands)
	- [ ] Domination
	- [ ] Sparseness
	- [ ] Volume
- [x] Handle startloop and endloop in rules.
- [X] Parsing the "Sounds" section.
- [x] Parsing the "CollisionLayers" section.
- [x] Parsing the "WinConditions" section.
- [x] Parsing the "Rules" section.
- [x] Parsing the "Prelude" section.
- [x] Parsing the "Objects" section.
- [x] Parsing the "Legend" section.
- [x] Parsing the "Levels" section.
- [x] Script to download PuzzleScript sources from the Gallery.
- [x] Handle block comments.
- [x] Indexing a script should automatically index its sections field.

Notes
-----

