__author__ = 'Chong-U Lim, culim@mit.edu'

import urllib2,re,json,os

from bs4 import BeautifulSoup
from puzzlescript import Script
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

	# Test 1: Open a puzzle script file and convert to PuzzleScript obj.
	f = open("../scripts/limerick.txt")
	txt = f.read()
	script = Script(txt)
	f.close()

	# Test 2: Try opening all the scripts in the '../scripts' directory.
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







