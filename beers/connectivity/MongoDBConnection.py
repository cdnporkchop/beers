import sys
import os
sys.path.append(os.path.abspath('..'))

from beers.connectivity import Settings
from pymongo import MongoClient
import datetime

class MongoDBConnection:
    def __init__(self):
        self.mongoDBConf = {
            "hostURL"               : "mongodb://" + Settings.server_ip + ":27017/",
            "db"                    : "Beers",
            "BeersCollection"       : "beers"
        }

    def get_db(self):
        client = MongoClient(self.mongoDBConf['hostURL'])
        db = client[self.mongoDBConf['db']]
        return db

    def get_beer_collection(self):
        return self.get_db()[self.mongoDBConf['BeersCollection']]

    def insert_beer(self, beer_json):
        beer_name = beer_json["name"]
        print '  [x]  Beer: ', beer_name
        collection = self.get_beer_collection()
        print "Inserted: ", collection.update({'name': beer_name}, beer_json, upsert=True)

    def update_beer(self, mongo_id, school):
        collection = self.get_beer_collection()
        id = collection.update({'_id':mongo_id}, {"$set": school}, upsert=True)
        return id.get('updatedExisting')

    def print_all_beers(self):
        collection = self.get_beer_collection()
        print collection.find().count(), 'documents in collection'
        for school in collection.find():
            print school


mongo = MongoDBConnection()
data = {
    "sch_number": "686263",
    "date": "2015-06-04 11:07:21.722000",
    "name": "All Saints Catholic Elementary School (Unionville)",
    "modified": datetime.datetime.utcnow()
}
#id = db.test_collection.insert_one(data).inserted_id
#mongo.insertElementarySchool(school);
#mongo.printAllSchools();


#col = mongo.getElementarySchoolCollection()
#id = col.find_one({"sch_number": "686263qwrewqrwqre"})
#if id is None:
#    print "Doesn't exist"
#else:
#    print id # id.get("_id")


#print db.test_collection.find_one()
#-----------------------------------------------------------
#mongo = MongoDBConnection()
#collection = mongo.getElementarySchoolCollection()
#entry = collection.find_one({"modified": datetime.datetime(2015, 6, 4, 19, 43, 58, 236000)})
#print "found : ", entry
#data = {
#    "sch_number": "686263b",
#    "date": "2015-06-04 11:07:21.722000",
#    "name": "All Saints Catholic Elementary School (Unionville)",
#    "modified": datetime.datetime.utcnow()
#}
#mongo.insertElementarySchool(data)
#mongo.insertElementarySchool(data)
#-----------------------------------------------------------



#collection.update({'_id':entry.get("_id")}, {"$set": data}, upsert=False)
#entry = collection.find_one({"_id":  entry.get("_id")})
#print "found2: ", entry

