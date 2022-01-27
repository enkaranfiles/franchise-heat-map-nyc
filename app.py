from ast import literal_eval
import json
from flask import Flask, request, render_template
from flask_cors import CORS
import pandas as pd
from sklearn.cluster import KMeans
from conf.conf import db_query_alias
from flask_pymongo import pymongo


app = Flask(__name__)
CORS(app)


CONNECTION_STRING = "mongodb+srv://eneskar:Sherlock1.@cluster0.s8rs2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')


def read(query):
    query = {query: {'$exists': 1}}

    documents = user_collection.find(query)
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return response


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/filter_info', methods=['GET'])
def filter_information():
    selected_brands = literal_eval(request.args.get('selectedBrands').replace(" ","").replace("\'",""))
    brand = selected_brands[0]
    query = db_query_alias[brand]
    data_points = read(query)[0][query]
    centers = get_frequency(data_points)
    return json.dumps(centers)

#for google heatmap -- testing purpose
@app.route('/show_all', methods=['GET'])
def show_all_franchise():
    selected_brands = literal_eval(request.args.get('selectedBrands').replace(" ","").replace("\'",""))

    with open('./Database/{}.json'.format(selected_brands[0])) as json_file:
        response_data = json.load(json_file)

    filtered_response = []
    for data in response_data:
        if data['name'] in request.args.get('selectedBrands'):
            response = {
                "location": data['geometry']['location']
            }
            filtered_response.append(response)

    return json.dumps(filtered_response)

def get_frequency(filtered_response):
    location = []
    for data in filtered_response:
        temp = {
            "lat": data["location"]["lat"],
            "lng": data["location"]["lng"]
        }
        location.append(temp)
    df = pd.DataFrame(location)

    kmeans = KMeans(n_clusters=3, max_iter=1000, init='k-means++')
    weighted_kmeans_clusters = kmeans.fit(df.values)  # Compute k-means clustering.
    df['cluster_label'] = kmeans.predict(df.values)
    centers = kmeans.cluster_centers_  # Coordinates of cluster centers.
    clusters = 3
    sorted_frequency = df["cluster_label"].value_counts()[:clusters].index.tolist()

    result = [
        {"location":
            {
                "lat": centers[sorted_frequency[0]][0],
                "lng": centers[sorted_frequency[0]][1]
            }},
        {"location":
            {
                "lat": centers[sorted_frequency[1]][0],
                "lng": centers[sorted_frequency[1]][1]
            }},
        {"location":
            {
                "lat": centers[sorted_frequency[2]][0],
                "lng": centers[sorted_frequency[2]][1]
            }}
    ]

    return result


if __name__ == '__main__':
    app.run()
