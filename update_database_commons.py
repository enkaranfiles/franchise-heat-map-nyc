from conf.conf import new_york_city, \
    burger_king, \
    mcdonalds, \
    shake_shack, \
    five_guys, districts

import requests
import json
import time

manhattan_lat = new_york_city["manhattan"]["lat"]
manhattan_lng = new_york_city["manhattan"]["lng"]
brooklyn_lat = new_york_city["brooklyn"]["lat"]
brooklyn_lng = new_york_city["brooklyn"]["lng"]
queens_lat = new_york_city["queens"]["lat"]
queens_lng = new_york_city["queens"]["lng"]
bronx_lat = new_york_city["bronx"]["lat"]
bronx_lng = new_york_city["bronx"]["lng"]


class UpdateDatabase():
    def __init__(self, key):
        self.__key = key

    def get_data_of_burger_king(self):
        params = {}

        burger_kings = []
        shops = []
        for district in districts:
            shop = []
            prep_query = burger_king[district]
            lat = new_york_city[district]["lat"]
            lng = new_york_city[district]["lng"]
            endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + prep_query + "&" \
                                                                                                                "location=" + str(
                lat) + "," + str(lng) + "&region=us&type=restaurant,food,point_of_interest,establishment&" \
                                                    "key=" + self.__key
            res = requests.get(endpoint_url)
            results = json.loads(res.content)
            shop.extend(results['results'])
            while "next_page_token" in results:
                params["pagetoken"] = results["next_page_token"]
                res = requests.get(endpoint_url, params=params)
                results = json.loads(res.content)
                shop.extend(results["results"])
                time.sleep(2)
            print(district)
            print(len(shop))
            print("--------------")
            for index in shop:
                shops.append(index)

        for location in shops:
            burger_kings.append(location)

        print(len(burger_kings))
        print(burger_kings)

        with open('./Updated-Database/BurgerKing.json', 'w') as fp:
            json.dump(burger_kings, fp)

    def get_data_of_mcdonalds(self):
        params = {}

        mcdonalds_list = []
        shops = []
        for district in districts:
            shop = []
            prep_query = mcdonalds[district]
            lat = new_york_city[district]["lat"]
            lng = new_york_city[district]["lng"]
            endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + prep_query + "&" \
                                                                                                              "location=" + str(
                lat) + "," + str(lng) + "&region=us&type=restaurant,food,point_of_interest,establishment&" \
                                        "key=" + self.__key
            res = requests.get(endpoint_url)
            results = json.loads(res.content)
            shop.extend(results['results'])
            while "next_page_token" in results:
                params["pagetoken"] = results["next_page_token"]
                res = requests.get(endpoint_url, params=params)
                print(res.content)
                results = json.loads(res.content)
                shop.extend(results["results"])
                time.sleep(2)
            print(district)
            print(len(shop))
            print("--------------")
            for index in shop:
                shops.append(index)

        for location in shops:
            mcdonalds_list.append(location)

        with open('./Updated-Database/McDonalds.json', 'w') as fp:
            json.dump(mcdonalds_list, fp)

    def get_data_of_shake_shack(self):
        params = {}

        shakeshack = []
        shops = []
        for district in districts:
            shop = []
            prep_query = shake_shack[district]
            lat = new_york_city[district]["lat"]
            lng = new_york_city[district]["lng"]
            endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + prep_query + "&" \
                                                                                                              "location=" + str(
                lat) + "," + str(lng) + "&region=us&type=restaurant,food,point_of_interest,establishment&" \
                                        "key=" + self.__key
            res = requests.get(endpoint_url)
            results = json.loads(res.content)
            shop.extend(results['results'])
            while "next_page_token" in results:
                params["pagetoken"] = results["next_page_token"]
                res = requests.get(endpoint_url, params=params)
                print(res.content)
                results = json.loads(res.content)
                shop.extend(results["results"])
                time.sleep(2)
            print(district)
            print(len(shop))
            print("--------------")
            for index in shop:
                shops.append(index)

        for location in shops:
            shakeshack.append(location)

        with open('./Updated-Database/ShakeShack.json', 'w') as fp:
            json.dump(shakeshack, fp)


    def get_data_of_five_guys(self):
        params = {}

        fiveguys = []
        shops = []
        for district in districts:
            shop = []
            prep_query = five_guys[district]
            lat = new_york_city[district]["lat"]
            lng = new_york_city[district]["lng"]
            endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + prep_query + "&" \
                                                                                                              "location=" + str(
                lat) + "," + str(lng) + "&region=us&type=restaurant,food,point_of_interest,establishment&" \
                                        "key=" + self.__key
            res = requests.get(endpoint_url)
            results = json.loads(res.content)
            shop.extend(results['results'])
            while "next_page_token" in results:
                params["pagetoken"] = results["next_page_token"]
                res = requests.get(endpoint_url, params=params)
                print(res.content)
                results = json.loads(res.content)
                shop.extend(results["results"])
                time.sleep(2)
            print(district)
            print(len(shop))
            print("--------------")
            for index in shop:
                shops.append(index)

        for location in shops:
            fiveguys.append(location)

        with open('./Updated-Database/FiveGuys.json', 'w') as fp:
            json.dump(five_guys, fp)
