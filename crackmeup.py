import random

from randomjoke_dot_com import all_categories

from bs4 import BeautifulSoup
from selenium import webdriver

def jokescc():

	#selenium for PhantomJS
	driver = webdriver.PhantomJS()
	driver.get('http://jokes.cc.com/')
	#fetch HTML source code after rendering
	soupFromJokesCC = BeautifulSoup(driver.page_source)
	# locate the link in HTML
	randomJokeLink = soupFromJokesCC.findAll('div', {'id':'random_joke'})[0].findAll('a')[0]['href'] 
	# now go to that page to scrape the joke from there
	driver.get(str(randomJokeLink))
	#driver.quit()
	# Convert to BeautifulSoup object for easy parsing
	soupToGetJokeFrom = BeautifulSoup(driver.page_source)
	# Locate joke to parse as a list of <p>s
	jokeData = soupToGetJokeFrom.findAll('div', {'class':'content_wrap'})[0].findAll('p')
	# Concatenate them into one string and get the joke
	joke = ''
	for sectionsInJokes in jokeData:
		currSection = str(sectionsInJokes)
		#Remove <p>, </p> and whitespaces
		joke += currSection[3:len(currSection)-4].strip()+"\n"
	print joke

def randomjokescc():
	categories = {'Random':'haha', 'One Liners':'oneliners', 'True Stories':'news',
	'Signs of Our Times':'signs', 'Nerdy Jokes':'nerd','Quotes':'quotes',
	'Professional':'professional', 'Light Bulb':'lightbulb', 
	'Gender Battles':'couples', 'Riddles':'riddles', 'Religion':'religion',
	'Gross':'gross', 'Blondes':'blonde', 'Politics':'politics', 'Just do it':'doit',
	'Laws':'laws', 'PG 13':'dirty', 'Racist':'ethnic'}

	random_category = categories[random.choice(categories.keys())]

	print all_categories.getJoke(random_category)

jokescc()