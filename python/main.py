import urllib2,re,json

from bs4 import BeautifulSoup


def parse_url(url):
	return urllib2.urlopen(url).read()

if __name__ == "__main__":

	print "PuzzleScript Analyze"

	gallery_url = "http://puzzlescriptgallery.tumblr.com/"
	editor_url = "http://www.puzzlescript.net/editor.html?hack="
	play_url = "http://www.puzzlescript.net/play.html?p="

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




