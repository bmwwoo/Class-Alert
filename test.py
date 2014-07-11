from bs4 import BeautifulSoup
import urllib2


url = "http://www.registrar.ucla.edu/schedule/detselect.aspx?termsel=14F&subareasel=MATH+++&idxcrs=0033A+++"
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
#print soup.prettify()
print soup.find_all("td", {"class" : "dgd"})