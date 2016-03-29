from randomjoke_dot_com import all_categories

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
	print jokeData

def randomjokesDotcom():
	categories = {'Random':'haha', 'One Liners':'oneliners', 'True Stories':'news',
	'Signs of Our Times':'signs', 'Nerdy Jokes':'nerd','Quotes':'quotes',
	'Professional':'professional', 'Light Bulb':'lightbulb', 
	'Gender Battles':'couples', 'Riddles':'riddles', 'Religion':'religion',
	'Gross':'gross', 'Blondes':'blonde', 'Politics':'politics', 'Just do it':'doit',
	'Laws':'laws', 'PG 13':'dirty', 'Racist':'ethnic'}

	random_category = categories[random.choice(categories.keys())]

	print all_categories.getJoke(random_category).strip()

whichSite = randint(0,1)
if whichSite:
	jokesDotCCDotcom()
else:
	randomjokesDotcom()
