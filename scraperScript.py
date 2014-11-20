import imp
import json
import pymongo
from pprint import pprint
import courseGraphData

def CourseLinks():
	term = 'W15'
	courseLinkFilename =  './ClassLinks/allLinks' + term + '.json'
	courseLinkJSON = open(courseLinkFilename)
	allCourseLinks = json.load(courseLinkJSON)
	return allCourseLinks


keys = imp.load_source('module.name', './APIKeys/APIKeys.py')
#client = pymongo.MongoClient(keys.MONGOKEY())
#db = client.get_default_database()


allCourseLinks = CourseLinks()
courseDict = {}
classes = []
for subject in allCourseLinks['Computer Science']:
	classes.append(courseGraphData.createCourse(subject))
courseDict['Computer Science'] = classes
#pprint(courseDict)
for team in courseDict['Computer Science']:
	for a in team:
		for b in a:
			pprint(b)
			'''for c in b:
				for metaData in c:
					#print "Title:\t%s\nEnrolled Capacity:\t%d\nEnrolled Now:\t%d" % (metaData['title'], metaData['enrolledCapacity'], metaData['enrolled'])
'''
pprint( courseDict['Computer Science'][2]['COM SCI 32 INTRO TO COM SCI 2'][0]['enrolled'] )
#	print "Title:\t%s\nEnrolled Capacity:\t%d\nEnrolled Now\t%d" % (team['title'], team['enrolledCapacity'], team['enrolled'])

#client.close()