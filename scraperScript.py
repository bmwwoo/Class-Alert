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

client = pymongo.MongoClient(keys.MONGOKEY())
db = client.get_default_database()




allCourseLinks = CourseLinks()
courseGraphData.createCourse("http://www.registrar.ucla.edu/schedule/detselect.aspx?termsel=15W&subareasel=PHYSICS&idxcrs=0001C+++")
