import pymongo
from bson.objectid import ObjectId




# Connection string to your MongoDB Atlas cluster


connection_string = "mongodb+srv://superfapi2000:faro1234@cluster0.hnbfqca.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)


def updateMongoDBStorage(day,data):
    #first get the day present in mongo db Storage
    db = client["test"]
    #Check if the collection already exists:
    if day not in db.list_collection_names():
        print(day)
        db.create_collection(day)
    #insert Data into collections
    collection = db[day]
    document = serialize(data)
    collection.insert_one(document)

def getMongoData_ApointmentsDays():
    db = client["test"]
    collection_names = db.list_collection_names()
    return collection_names



def getMongoData_ApointmentsDay(day):
    db = client["test"]
    # Select the collection
    collection = db[day]
    query= {'day': day}
     # Find the first document in the collection
    documents = collection.find(query)
    return documents
    
def serialize(data):
    document = {"day" :  data.day,
            "typeOfService" : data.typeOfService,
            "time" : data.time,
            "beggining" : data.beggining,
            "finish" : data.finish
            }
    return(document)
def deleteApointmentMongoData(day,objectID):
    
    # connect to your MongoDB Atlas database
    db = client["test"]
    collection = db[day]
    # define the filter for the item you want to remove (e.g., by _id)
    filter = {'_id': ObjectId(objectID)}
    # delete the item using the delete_one() method
    result = collection.delete_one(filter)
    print("Deleted", result.deleted_count, "document(s)")

    # print the result
def deleteApointmentMongoData(day,objectID):
    
    # connect to your MongoDB Atlas database
    db = client["test"]
    collection = db[day]
    # define the filter for the item you want to remove (e.g., by _id)
    filter = {'_id': ObjectId(objectID)}
    # delete the item using the delete_one() method
    result = collection.delete_one(filter)
    print("Deleted", result.deleted_count, "document(s)")

def editApointmentMongoData(day,data,objectID):
    # connect to your MongoDB Atlas database
    db = client["test"]
    collection = db[day]
    # define the filter for the item you want to remove (e.g., by _id)
    query = {'_id': ObjectId(objectID)}
    document = serialize(data)
    # delete the item using the delete_one() method
    collection.update_one(query,{'$set': document})
    print("Updated, 1 document")