import imp
import json
import pymongo
from pprint import pprint
import courseGraphData

def CourseLinks():
	TERM = 'W15'
	courseLinkFilename =  './ClassLinks/allLinks' + TERM + '.json'
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
courseDict["Computer Science"] = classes



'''
courseDict = {}
courseLoad = open("compsci.json")
courseDict = json.load(courseLoad)
'''


for compsci in courseDict['Computer Science']:
	for theClass in compsci:
		if compsci[theClass]:
			for theLecture in compsci[theClass]:
				print theLecture['title'] + '\t' + theLecture['professor'] + '\t' + str(theLecture['enrolledCapacity']) + '\t' + str(theLecture['enrolled'])
		
'''
		for b in a:
			print b
			for c in b:
				for metaData in c:
					#print "Title:\t%s\nEnrolled Capacity:\t%d\nEnrolled Now:\t%d" % (metaData['title'], metaData['enrolledCapacity'], metaData['enrolled'])

#pprint( courseDict['Computer Science'][2]['COM SCI 32 INTRO TO COM SCI 2'][0]['enrolled'] )
'''
'''
for(int i=0; i<numItems; i++)
{
	//For each Computer Science in courseDict
		//For each key (there will only be one key, i.e. COM SCI 32 INTO TO COM SCI 2)
			//For each item in the array of each key
				//print enrolled
}'''
#	print "Title:\t%s\nEnrolled Capacity:\t%d\nEnrolled Now\t%d" % (team['title'], team['enrolledCapacity'], team['enrolled'])

#client.close()