import urllib
from bs4 import BeautifulSoup

urlToRead = "http://jokes.cc.com";
handle = urllib.urlopen(urlToRead)
htmlGunk =  handle.read()
soup = BeautifulSoup(htmlGunk, "html.parser")
# print soup.prettify().encode('utf-8')
# Find out the exact position of the joke in the page
print soup.findAll('a', {'class':'random_link'})[0]
# The joke ends at the keyword 'Over'
#joke = jokeSectionText[:jokeSectionText.index('Over')].strip()
#return joke