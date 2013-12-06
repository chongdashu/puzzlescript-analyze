import urllib2,re,json

from bs4 import BeautifulSoup
from puzzlescript import Script


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

	txt = open("../scripts/basic.txt").read()
	script = Script(txt)







