import urllib
import random
from random import randint

from bs4 import BeautifulSoup


def jokesDotCCDotcom():

	'''to get random jokes from jokes.cc.com, we're going to use the API I dug up from their site (#sweg).
	-Send a request to http://jokes.cc.com/feeds/random/(any number between 1-6811)
	-Data recieved is in JSON
	-Extract this link, send a urllib request there and scrape out the joke from the HTML recieved
	'''
	randomLinkToGoToAPI = 'http://jokes.cc.com/feeds/random/' + str(randint(1, 6811))
	JSONData = urllib.urlopen(randomLinkToGoToAPI).read()
	#parse data
	parsedJokeLink = JSONData[JSONData.index('http') : JSONData.index('","queryString')].replace('\\',"")
	#Now send a request to parse this random joke link
	handle = urllib.urlopen(parsedJokeLink)
	htmlGunk =  handle.read()
	soup = BeautifulSoup(htmlGunk, "html.parser")
	jokeData = soup.findAll('div', {'class':'content_wrap'})[0].get_text()
	if 'Next' in jokeData:
		jokeData = jokeData[jokeData.index('Next')+5:]
	return jokeData
	

def randomjokesDotcom():
	categories = {'Random':'haha', 'One Liners':'oneliners', 'True Stories':'news',
	'Signs of Our Times':'signs', 'Nerdy Jokes':'nerd','Quotes':'quotes',
	'Professional':'professional', 'Light Bulb':'lightbulb', 
	'Gender Battles':'couples', 'Riddles':'riddles', 'Religion':'religion',
	'Gross':'gross', 'Blondes':'blonde', 'Politics':'politics', 'Just do it':'doit',
	'Laws':'laws', 'PG 13':'dirty', 'Racist':'ethnic'}

	category = categories[random.choice(categories.keys())]

	urlToRead = "http://www.randomjoke.com/topic/" + (category) + (".php")
	handle = urllib.urlopen(urlToRead)
	htmlGunk =  handle.read()
	soup = BeautifulSoup(htmlGunk, "html.parser")
	#print soup.prettify().encode('utf-8')
	# Find out the exact position of the joke in the page
	jokeSectionText = soup.body.findAll('tr')[1].findAll('td')[2].findAll('p')[1].get_text() # magic
	# The joke ends at the keyword 'Over'
	joke = jokeSectionText[:jokeSectionText.index('Over')].strip()
	return joke

whichSite = randint(0,1)
if whichSite:
	print "\n" + jokesDotCCDotcom()
	print "\nSource - jokes.cc.com"

else:
	print "\n" + randomjokesDotcom()
	print "\nSource - randomjoke.com"
