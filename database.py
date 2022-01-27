
from flask_pymongo import pymongo
from app import app
import json


CONNECTION_STRING = "mongodb+srv://eneskar:Sherlock1.@cluster0.s8rs2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')


#test to insert data to the data base
@app.route("/test")
def insert_db():
    burger_king = {}
    with open('./Database/{}.json'.format("FiveGuys")) as json_file:
        response_data = json.load(json_file)

    filtered_response = []
    for data in response_data:
        response = {
                "location": data['geometry']['location']
        }
        filtered_response.append(response)

    burger_king = {
        "five-guys" : filtered_response
    }
    user_collection.insert_one(burger_king)
    print("success")


def read():
    query = {'burger-king': {'$exists': 1}}

    documents = user_collection.find(query)
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return response


insert_db()
"""
#test()
response = read()
print(response[0]["mcdonalds"])
"""
