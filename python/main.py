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

if __name__ == "__main__":

	print "PuzzleScript Analyze"

	test1 = True
	test2 = True

	scripts = []
	scriptsfolderpath = os.path.normpath('../scripts') + os.sep

	# Test 1: Open a puzzle script file and convert to PuzzleScript obj.
	if test1:
		f = open("../scripts/basic.txt")
		txt = f.read()
		script = Script(txt)
		f.close()

	# Test 2: Try opening all the scripts in the '../scripts' directory.
	if test2:
		
		for filename in os.listdir(scriptsfolderpath):
			print ("Parsing: %s\n-------------") %(filename)
			filepath = scriptsfolderpath + filename
			
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

	# Test 4: Level Flood-Fill walls with question-marks.
	level3 = PSLevel.string_to_level(string1, level1.width, level1.height)
	level3.fill(2,3,None,'?')

	# Test 5: Load microban script.
	microban = scripts[os.listdir(scriptsfolderpath).index('microban.txt')]
	atlas =  scripts[os.listdir(scriptsfolderpath).index('atlas.txt')]
	# Test 6: Analyze selected scripts
	for scriptName in ['microban','blockfaker','limerick', 'atlas', 'colourchained']:
		script = scripts[os.listdir(scriptsfolderpath).index(scriptName+'.txt')]
		analyer = Analyzer(script)
		analyer.printStats(scriptName)









