import json

# restaurants = {}
# # read from zomatoData.json
# with open('zomatoData.json', 'r') as f:
#     restaurants = json.load(f)
# # if avgCost is missing, put popularDishes in knownFor and knownFor in avgCost and empty list in popularDishes
# for link in restaurants:
#     for restaurant in restaurants[link]:
#         if restaurant['avgCost'] == "":
#             try:
#                 restaurant['avgCost'] = restaurant['knownFor'][0].split(' ')[0].split('₹')[1]
#                 restaurant['knownFor'] = restaurant['popularDishes']
#                 restaurant['popularDishes'] = []
#             except:
#                 try:
#                     restaurant['avgCost'] = restaurant['popularDishes'][0].split(' ')[0].split('₹')[1]
#                     restaurant['popularDishes'] = []
#                     restaurant['knownFor'] = []
#                 except:
#                     restaurant['avgCost'] = "0"
# # write to zomatoData.json
# with open('zomatoData.json', 'w') as f:
#     json.dump(restaurants, f, indent=4)

# # read from zomatoData.json
with open('zomatoData.json', 'r') as f:
    restaurants = json.load(f)

# convert json to csv
with open('zomatoData.csv', 'w') as f:
    f.write('Name,Address,Phone,Rating,AvgCost,Known For,Popular Dishes,Cuisine,Reviews\n')
    for link in restaurants:
        for restaurant in restaurants[link]:
            f.write(restaurant['name'] + ',')
            f.write("\"" + restaurant['address'] + "\"" + ',')
            f.write(restaurant['phone'] + ',')
            f.write(restaurant['rating'] + ',')
            f.write(restaurant['avgCost'] + ',')
            temp = ''
            for item in restaurant['knownFor']:
                temp += item + '|'
            f.write(temp + ',')
            temp = ''
            for item in restaurant['popularDishes']:
                temp += item + '|'
            f.write(temp + ',')
            temp = ''
            for item in restaurant['cuisine']:
                temp += item + '|'
            f.write(temp + ',')
            temp = ''
            for item in restaurant['reviewHighlights']:
                temp += item + '|'
            f.write(temp + '\n')

            # f.write(restaurant['link'] + '\n')