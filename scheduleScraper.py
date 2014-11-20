import json
from bs4 import BeautifulSoup
import urllib2

def formatLink(url):
	url = url.replace(" ", "+")
	url = url.replace("&", "%26")
	return url

def linksOnPage(url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	allLinks = []
	for item in soup.find_all("option"):
		link = item.get("value")
		formattedLink = formatLink(link)
		totalURL = url.replace("crsredir", "detselect")
		totalURL = totalURL + "&idxcrs=" + formattedLink
		allLinks.append(totalURL)
	return allLinks



homeURL = "http://www.registrar.ucla.edu/schedule/schedulehome.aspx"
TERM = "15W"
#courseLinks = {"hi" : ["wee", "qua"], "raaa" : ["aar"]}


response = urllib2.urlopen(homeURL)
html = response.read()
soup = BeautifulSoup(html)
#print soup.prettify()
courseLinks = {}
subjects = []
for link in soup.find_all("option"):
	subjectCode = link.get("value")
	subject = link.get_text()
	if (subjectCode[0] == "1" or subjectCode[0] == "2"): #checks if it is a quarter term instead of subject
		#TODO eventually use this to add to another array to specify the URL by term
		continue
	subjectCode = formatLink(subjectCode)
	#everything is unicode
	
	subjectLink = "http://www.registrar.ucla.edu/schedule/crsredir.aspx?termsel=" + TERM + "&subareasel=" + subjectCode 
	print subjectLink
	classLinks = linksOnPage(subjectLink)
	courseLinks[subject] = classLinks

print json.dumps(courseLinks, sort_keys=True, indent=4, separators=(',', ': '))
'''for key, value in courseLinks.items()[0::]:
	print key 
	for x in value:
		print x

'''