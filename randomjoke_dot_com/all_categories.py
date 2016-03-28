import urllib
from bs4 import BeautifulSoup

def getJoke(category):
	urlToRead = "http://www.randomjoke.com/topic/" + (category) + (".php")
	handle = urllib.urlopen(urlToRead)
	htmlGunk =  handle.read()
	soup = BeautifulSoup(htmlGunk, "html.parser")
	print soup.prettify().encode('utf-8')
	# Find out the exact position of the joke in the page
	jokeSectionText = soup.body.findAll('tr')[1].findAll('td')[2].findAll('p')[1].get_text() # magic
	# The joke ends at the keyword 'Over'
	joke = jokeSectionText[:jokeSectionText.index('Over')].strip()
	return joke