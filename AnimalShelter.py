import pymongo
from pprint import pprint
from pymongo import MongoClient
from urllib.parse import quote_plus
from pymongo import ReturnDocument
import urllib.parse


class AnimalShelter(object):

#initialize the object 
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.


        self.client = pymongo.MongoClient('mongodb://' + username + ':' + password + '@localhost:35841', maxPoolSize=5)
        self.client.database_names()
        self.database = self.client['AAC']
        self.c = self.database['animals']

    def insertData(self, newAnimal):
        animalCollection = self.c
        try:
            result = animalCollection.insert_one(newAnimal).inserted_id
        except ValueError:
            return False
        
    def readAll(self):
        
        x = 0
        animalCollection = self.c
        cur = animalCollection.find()
        return cur


    def readData(self,animalView):
        animalCollection = self.c
        animal = animalCollection.find({"name": animalView})
        return animal

        
    def updateData(self,animalChange,attUpdate,newValue):
        animalCollection = self.c
#function used to find the document related to the dog 
#requested by the user and change the supplied attributes
        animalCollection.find_one_and_update(
            {"name":animalChange},
            {"$set":{attUpdate : newValue}},
            return_document=ReturnDocument.AFTER)
#printing the updated document 
        pprint(animalCollection.find_one({"name":newValue}))

#Brings in name of animal document that would like to be deleted
    def deleteData(self,animalDelete):
        animalCollection = self.c
        valuePair = {"name":animalDelete}
        animalCollection.delete_one(valuePair)
#check to ensure that the document of named animal
        if(animalCollection.find_one({"name":animalDelete}) != None):
            pprint("No document")







