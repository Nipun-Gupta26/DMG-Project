import json
import re
import requests

url = "https://api.foursquare.com/v3/places/search"

places = ['North-east', 'Shahdara','North-west','West','East','New Delhi','North','South','South-west','South-east','Central' ]

fsq_id = {}
review = {}

for place in places:
    
    params = {
        "query": "food",
        "near": place + " Delhi, Delhi, National Capital Territory of Delhi, India",
        'limit': 50,
    }

    headers = {
        "Accept": "application/json",
        "Authorization": "fsq3aKmQJtonyEpmbzzsI9MQuahphaID9r5Ub5l3DoGjQuE="
    }

    response = requests.request("GET", url, params=params, headers=headers)
    jsonObj = json.loads(response.text)
    venue_list = []
    
    for venue in jsonObj['results'] :
        venue_list.append(venue['fsq_id'])
        
    fsq_id[place] = venue_list
       
##data needed : rating , name , likes --> count 

# for place in fsq_id : 
#     print(fsq_id[place])
# print(fsq_id)

class Restaurant:
    def __init__(self, name : str, rating: float, likes: int, address: str, fsq_id: str, comments: list, price: str):
        self.name = name
        self.rating = rating
        self.likes = likes
        self.address = address
        self.fsq_id = fsq_id
        self.comments = comments
        self.price = price

    def __repr__(self):
        return f"Restaurant({self.name}, {self.rating}, {self.likes}, {self.address}, {self.fsq_id}, {self.comments}, {self.price})"
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def toDict(self):
        return self.__dict__

restaurants = {}
for place in fsq_id:
    restaurants[place] = []
    for venue in fsq_id[place]:
        url = "https://api.foursquare.com/v2/venues/" + venue
        params={
            'v':'20220920',
            'oauth_token':'C5UYLUIAVRGYAYNVZFPS1B5CO2FRKQDQRJ0AXRFMIUGOBKMB',
        }

        headers = {
            "Accept": "application/json",
            "Authorization": "fsq3aKmQJtonyEpmbzzsI9MQuahphaID9r5Ub5l3DoGjQuE="
        }
        try:
            response = requests.request("GET", url, params=params, headers=headers)
            jsonObj = json.loads(response.text)
            try:
                name = jsonObj['response']['venue']['name']
            except:
                name = None
            try:
                rating = jsonObj['response']['venue']['rating']
            except:
                rating = None
            try:
                likes = jsonObj['response']['venue']['likes']['count']
            except:
                likes = None
            try:
                address = jsonObj['response']['venue']['location']['address']
            except:
                address = None
            try:
                groups = jsonObj['response']['venue']['tips']['groups']
                comments = []
                for group in groups:
                    for item in group['items']:
                        comments.append(item['text'])
            except:
                comments = None
            try:
                
                price = jsonObj['response']['venue']['price']['message']
            except:
                price = None
            restaurants[place].append(Restaurant(name, rating, likes, address, venue, comments, price).toDict())
            print(restaurants[place])
            # print(restaurants[place])
            # write in file
            # with open('restaurants.json', 'w') as f:
            #     json.dump(restaurants, f)
        except:
            print("error in " + venue)

##To correct : 
##Not recieving the comments
##Not recieving the price 

# write in json file
with open('restaurants.json', 'w') as f:
    json.dump(restaurants, f)

# for place in fsq_id : 
#     for venue in fsq_id[place] : 
#         review[venue] = {}
#         url = "https://api.foursquare.com/v2/venues/" + venue
#         params={
#             'v':'20220920',
#             'oauth_token':'C5UYLUIAVRGYAYNVZFPS1B5CO2FRKQDQRJ0AXRFMIUGOBKMB'
#         }

#         headers = {
#             "Accept": "application/json",
#             "Authorization": "fsq3aKmQJtonyEpmbzzsI9MQuahphaID9r5Ub5l3DoGjQuE="
#         }


#         response = requests.request("GET", url, params=params, headers=headers)
#         jsonObj = json.loads(response.text)
