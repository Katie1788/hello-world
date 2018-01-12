from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorsUSA'
COLLECTION_NAME = 'projects'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False}
# above block of code credited to Richard Dalton on slack

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
        collection = connection[DBS_NAME][COLLECTION_NAME]
        projects = collection.find(projection=FIELDS)
        for project in projects
            print project
