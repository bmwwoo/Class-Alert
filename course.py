from bs4 import BeautifulSoup
import urllib2

class Course:
	courseCount = 0
	def update():
		"""TODO"""
		'''basically make it check the enrolled vs enCapacity vs waitlist and if the numbers don't match, update it and alert system. 
		this probably will be by a bool if it should be checked in the main. the push notification will also be in the main. All this function
		should do is change the number.'''
	def __init__(self, name):
		#courseCount += 1
		self.title = name
		self.type = "LEC"
		self.prof = ""
		self.sectionNumber = ""
		self.days = ""
		self.startTime = ""
		self.endTime = ""
		self.building = ""
		self.room = ""
		self.enrolled = ""
		self.enrolledCapacity = ""
		self.waitlist = ""
		self.WLCapacity = ""
		self.Status = ""
		self.discussions = []
	#bool should check?
class Discussion(Course):
	discussionCount = 0
	def update():
		'''TODO'''

	def __init__(self, name):	
		self.id = ""
		self.type = "DIS"
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
	#soup = BeautifulSoup(open("physics.html"))
	course = {}
	title = findTitle(soup)
	lectures = []
	lecturePlaceholder = -1
	#creates nubmer of lectures and discussions
	for courseTitle in soup.find_all("td", {"class" : "dgdClassDataActType"}):
		courseType = courseTitle.get_text()
		courseType = "".join(courseType.split())
		if courseType == "LEC":
			lecturePlaceholder += 1
			lec = Course(title)
			lectures.append(lec)
		elif courseType == "DIS":
			dis = Discussion(title)
			lectures[lecturePlaceholder].discussions.append(dis)
	i = 0
	#assigns all staff to the lectures
	for lec in soup.find_all("span", {"class" : "fachead"}):
		staff = lec.get_text()
		staff = " ".join(staff.split())
		lectures[i].prof = staff
		i += 1
	#creates a list of the section numbers of lectures and discussions (ie. 1 - 5E)
	__SectionNumbers = findData(soup, "dgdClassDataSectionNumber")
	#creates a list of the dats the lectures and discussions meet on (ie. TWF)
	__Days = findData(soup, "dgdClassDataDays")
	#creates a list of the start times (11:00 AM)
	__StartTimes = findData(soup, "dgdClassDataTimeStart")
	__EndTimes = findData(soup, "dgdClassDataTimeEnd")
	__Building = findData(soup, "dgdClassDataBuilding")
	__Room = findData(soup, "dgdClassDataRoom")
	__Enrolled = findData(soup, "dgdClassDataEnrollTotal")
	__EnrolledCapacity = findData(soup, "dgdClassDataEnrollCap")
	__Waitlist = findData(soup, "dgdClassDataWaitListTotal")
	__WLCapacity = findData(soup, "dgdClassDataWaitListCap")
	__Status = findData(soup, "dgdClassDataStatus")
	#assignment of all data to the list of classes	
	i = 0
	for lec in lectures:
		#outside of inner loop to assign it to the lecture
		lec.sectionNumber = __SectionNumbers[i]
		lec.days = __Days[i]
		lec.startTime = __StartTimes[i]
		lec.endTime = __EndTimes[i]
		lec.building = __Building[i]
		lec.room = __Room[i]
		lec.enrolled = __Enrolled[i]
		lec.enrolledCapacity = __EnrolledCapacity[i]
		lec.waitlist = __Waitlist[i]
		lec.WLCapacity = __WLCapacity[i]
		lec.Status = __Status[i]
		for dis in lec.discussions:
			i += 1
			dis.sectionNumber = __SectionNumbers[i]
			dis.days = __Days[i]
			dis.startTime = __StartTimes[i]
			dis.endTime = __EndTimes[i]
			dis.building = __Building[i]
			dis.room = __Room[i]
			dis.enrolled = __Enrolled[i]
			dis.enrolledCapacity = __EnrolledCapacity[i]
			dis.waitlist = __Waitlist[i]
			dis.WLCapacity = __WLCapacity[i]
			dis.Status = __Status[i]
		i += 1
	course[title] = lectures #course should be a global? probably returns just lectures and course should be what it returns into
	i = 0
	while i < 5:
		print "%s\t%s\n%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (course[title][i].title, course[title][i].prof, course[title][i].type, course[title][i].sectionNumber, course[title][i].days, course[title][i].startTime, course[title][i].endTime, course[title][i].building, course[title][i].room, course[title][i].enrolled, course[title][i].enrolledCapacity, course[title][i].waitlist, course[title][i].WLCapacity, course[title][i].Status)
		for x in course[title][i].discussions:
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (x.type, x.sectionNumber, x.days, x.startTime, x.endTime, x.building, x.room, x.enrolled, x.enrolledCapacity, x.waitlist, x.WLCapacity, x.Status)
		i += 1
	#print soup.find_all("td", {"class" : "dgd"})
	return course
