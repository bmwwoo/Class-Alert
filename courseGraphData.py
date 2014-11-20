import json
from bs4 import BeautifulSoup
import urllib2


def findTitle(soup):
#finds title of course since it is always the second coursehead
	isTitle = False
	for x in soup.find_all("span" ,{"class" : "coursehead"}):
		if isTitle:
			title = x.get_text()
			title = " ".join(title.split()) #removes extra spaces
			return title
		isTitle = True

def findData(soup, title):
	data = []
	for item in soup.find_all("td", {"class" : title}):
		response = item.get_text()
		response = "".join(response.split())
		data.append(response)
	return data


def createCourse(url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	courseDict = {}
	title = findTitle(soup)
	lectures = []
	counter = 0
	lectureCounter = []
	#creates nubmer of lectures and discussions
	for courseTitle in soup.find_all("td", {"class" : "dgdClassDataActType"}):
		courseType = courseTitle.get_text()
		courseType = "".join(courseType.split())
		if courseType == "LEC":
			theLec = {'title' : title, 'professor' : '', 'enrolled' : [], 'enrolledCapacity' : ''}
			lectures.append(theLec)
			lectureCounter.append(counter)
			counter += 1
		if courseType == "DIS":
			counter += 1

	Enrolled = findData(soup, "dgdClassDataEnrollTotal")
	EnrolledCapacity = findData(soup, "dgdClassDataEnrollCap")
	professorList = []
	for lec in soup.find_all("span", {"class" : "fachead"}):
		staff = lec.get_text()
		staff = " ".join(staff.split())
		professorList.append(staff)
	#assignment of all data to the list of classes	
	i = 0
	for lec in lectures:
		counter = lectureCounter[i]
		lec['enrolled'] = int(Enrolled[counter])
		lec['enrolledCapacity'] = int(EnrolledCapacity[counter])
		lec['professor'] = professorList[i]
		i += 1

	courseDict[title] = lectures #course should be a global? probably returns just lectures and course should be what it returns into
	
	#print json.dumps(courseDict, sort_keys=True, indent=4, separators=(',', ': '))
	return courseDict
