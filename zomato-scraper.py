import csv
import json
from symbol import except_clause
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

# Set up the browser
# browser = webdriver.Chrome(ChromeDriverManager().install())
# links = ['https://www.zomato.com/ncr/delivery-in-south-delhi', 'https://www.zomato.com/ncr/delivery-in-north-delhi',
#          'https://www.zomato.com/ncr/delivery-in-east-delhi', 'https://www.zomato.com/ncr/delivery-in-west-delhi', 'https://www.zomato.com/ncr/delivery-in-central-delhi']
# restaurants = {}
# for link in links:
#     browser.get(link)
#     time.sleep(2)
#     restaurants[link] = set()

#     rows = browser.find_elements(By.CSS_SELECTOR, ".sc-doWzTn")
#     while len(rows) < 3:
#         browser.execute_script(
#             "window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
#         rows = browser.find_elements(By.CSS_SELECTOR, ".sc-1mo3ldo-0")
#         print(len(rows))

#     # find all links hrefs

#     a_links = browser.find_elements_by_tag_name('a')
#     # for a in a_links:

#     print(len(a_links))
#     # filter links having /order in them
#     iteration = 0
#     for a in a_links:
#         print(iteration)
#         href = a.get_attribute('href')
#         try:
#             if 'order' in href:
#                 restaurants[link].add(href)
#         except:
#             pass
#         iteration += 1
#     restaurants[link] = list(restaurants[link])
#     # for row in rows:
#     #     # print all elements in row
#     #     try:
#     #         # print(row.find_elements_by_tag_name("a"))
#     #         restaurants[link].add(row.find_element_by_tag_name("a").get_attribute("href"))
#     #     except:
#     #         print("Error")
#     #         pass
#         # try:
#         #     jumbo_tracker = row.find_element(By.CSS_SELECTOR, ".jumbo-tracker")
#         #     if jumbo_tracker:
#         #         a_link = jumbo_tracker.find_element(By.HTML, "a")
#         #         restaurants[link].append(a_link.get_attribute("href"))
#         #     else:
#         #         print("No jumbo tracker")
#         # except:
#         #     print("No jumbo tracker")
#         #     pass
#     # break

# print(restaurants)
# print(len(restaurants))
# # add to json file named zomato.json
# with open('zomato.json', 'w') as f:
#     json.dump(json.dumps(restaurants), f)


# - Created a web scraper using python and selenium to scrape data from zomato website.
# - The script is able to go to five different locations and scrape the data from the page.
# - Challenges:
#     - The page is dynamic and the data is loaded using lazy loading. We have to scroll down to load more data.
#     - The data is loaded in a grid format and we have to extract the data from each grid.
#     - The scraper needs to visit multiple pages and extract data from each page. This requires a lot of time


with open('zomato.json') as f:
    data = json.load(f)
    print(data)

browser = webdriver.Chrome(ChromeDriverManager().install())
restaurants = {}
for link in data:
    restaurants[link] = []
    for href in data[link]:
    # href = data[link][0]
        browser.get(href)
        time.sleep(2)
        try:
            name = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div/main/div/section[3]/section/section/div/div/div/h1').text
        except:
            name = ""
        try:
            rating = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div/main/div/section[3]/section/section/div/div/div/section/div[3]/div[1]/div/div/div[1]').text
        except:
            rating = "0"
        browser.find_element(by=By.XPATH, value='/html/body/div[1]/div/main/div/article/div/section/section/div[1]/h2/a').click()
        time.sleep(2)
        try:
            address = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div/main/div/section[4]/section/article/section/p').text
        except:
            address = ""
        try:
            phone = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div/main/div/section[4]/section/article/p').text.split('#')[0]
        except:
            phone = ""
        try:
            popularDishes = browser.find_element(by = By.XPATH, value='/html/body/div[1]/div/main/div/section[4]/section/section/article[1]/section[1]/p[1]').text
            popularDishes = popularDishes.split(', ')
        except:
            popularDishes = []
        try:
            knownFor = browser.find_element(by = By.XPATH, value='/html/body/div[1]/div/main/div/section[4]/section/section/article[1]/section[1]/p[2]').text
            knownFor = knownFor.split(', ')
        except:
            knownFor = []
        try:
            avgCost = browser.find_element(by = By.XPATH, value='/html/body/div[1]/div/main/div/section[4]/section/section/article[1]/section[1]/p[3]').text.split(' ')[0].split('₹')[1]
        except:
            avgCost = ""
        try:
            cuisineSection = browser.find_element(by = By.XPATH, value='/html/body/div[1]/div/main/div/section[4]/section/section/article[1]/section[1]/section[3]')
            cuisine = cuisineSection.find_elements(by = By.TAG_NAME, value='a')
            cuisine = [c.text for c in cuisine]
        except:
            cuisine = []
        try:
            reviewSection = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div/main/div/section[4]/section/section/section[2]/div')
            reviewHighlights = reviewSection.find_elements(by=By.TAG_NAME, value='span')
            reviewHighlights = [r.text for r in reviewHighlights]
            if 'Write a Review' in reviewHighlights:
                reviewHighlights.remove('Write a Review')
        except:
            reviewHighlights = []
        print(name, rating, address, phone, popularDishes, knownFor, avgCost, cuisine, reviewHighlights)
        # write to json file
        restaurants[link].append({
            'name': name,
            'rating': rating,
            'address': address,
            'phone': phone,
            'popularDishes': popularDishes,
            'knownFor': knownFor,
            'avgCost': avgCost,
            'cuisine': cuisine,
            'reviewHighlights': reviewHighlights
        })
        with open('zomatoData.json', 'w') as f:
            json.dump(restaurants, f)
        # write to zomato.csv
    # with open('zomato.csv', 'a', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([name, rating, address, phone, popularDishes, knownFor, avgCost, cuisine, reviewHighlights])
        