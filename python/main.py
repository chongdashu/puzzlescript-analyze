__author__ = 'Chong-U Lim, culim@mit.edu'

import urllib2,re,json,os

from bs4 import BeautifulSoup
from puzzlescript import Script, PSLevel
from analyzer import Analyzer


def parse_url(url):
	return urllib2.urlopen(url).read()

def download_gallery_scripts():
	gallery_url = "http://puzzlescriptgallery.tumblr.com/"
	regex = re.compile("www.puzzlescript.net\/play.html\?p=([0-9]+)")
	gists_url = "https://api.github.com/gists/"

	html = parse_url(gallery_url)
	soup = BeautifulSoup(html)
	hrefs = [a['href'] for a in soup.find_all("a")]
	ids = [match.group(1) for match in [regex.search(href) for href in hrefs] if match]

	for id in ids:
		gist = gists_url+id
		content = json.JSONDecoder().decode(parse_url(gist))['files']['script.txt']['content']
		f = open('../scripts/'+id+".txt", 'w')
		f.write(content.encode('utf-8'))
		f.close()

def fill(level, row, col, oldchar, newchar):

	if oldchar == None:
		oldchar = level.definition[row][col]

	if not level.definition[row][col] == oldchar:
		return

	level.definition[row][col] = newchar

	if col > 0:
		fill(level, row, col-1, oldchar, newchar)

	if col < level.width-1:
		fill(level, row, col+1, oldchar, newchar)

	if row > 0:
		fill(level, row-1, col, oldchar, newchar)

	if row < level.height-1:
		fill(level, row+1, col, oldchar, newchar)

if __name__ == "__main__":

	print "PuzzleScript Analyze"

	test1 = True
	test2 = False

	# Test 1: Open a puzzle script file and convert to PuzzleScript obj.
	if test1:
		f = open("../scripts/basic.txt")
		txt = f.read()
		script = Script(txt)
		f.close()

	# Test 2: Try opening all the scripts in the '../scripts' directory.
	if test2:
		scripts = []
		folderpath = os.path.normpath('../scripts') + os.sep
		for filename in os.listdir(folderpath):
			print ("Parsing: %s\n-------------") %(filename)
			filepath = folderpath + filename
			
			temp_file = open(filepath)
			temp_txt = temp_file.read()
			temp_script = Script(temp_txt)
			
			scripts.append(temp_script)
			temp_file.close()

	# Test 3: Level serialization and conversion.
	level1 = script['levels'].levels[0]
	string1 = level1.serialize()
	string2 = PSLevel.level_to_string(level1)
	string1 == string2
	level2 = PSLevel.string_to_level(string2, level1.width, level1.height)

	# Test 4: Level Flood-Fill








