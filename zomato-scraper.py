import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import sys
import os

# Set up the browser
browser = webdriver.Chrome(ChromeDriverManager().install())
links = ['https://www.zomato.com/ncr/delivery-in-south-delhi', 'https://www.zomato.com/ncr/delivery-in-north-delhi',
         'https://www.zomato.com/ncr/delivery-in-east-delhi', 'https://www.zomato.com/ncr/delivery-in-west-delhi', 'https://www.zomato.com/ncr/delivery-in-central-delhi']
restaurants = {}
for link in links:
    browser.get(link)
    time.sleep(2)
    restaurants[link] = set()

    rows = browser.find_elements(By.CSS_SELECTOR, ".sc-doWzTn")
    while len(rows) < 3:
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        rows = browser.find_elements(By.CSS_SELECTOR, ".sc-1mo3ldo-0")
        print(len(rows))

    # find all links hrefs

    a_links = browser.find_elements_by_tag_name('a')
    # for a in a_links:

    print(len(a_links))
    # filter links having /order in them
    iteration = 0
    for a in a_links:
        print(iteration)
        href = a.get_attribute('href')
        try:
            if 'order' in href:
                restaurants[link].add(href)
        except:
            pass
        iteration += 1
    restaurants[link] = list(restaurants[link])
    # for row in rows:
    #     # print all elements in row
    #     try:
    #         # print(row.find_elements_by_tag_name("a"))
    #         restaurants[link].add(row.find_element_by_tag_name("a").get_attribute("href"))
    #     except:
    #         print("Error")
    #         pass
        # try:
        #     jumbo_tracker = row.find_element(By.CSS_SELECTOR, ".jumbo-tracker")
        #     if jumbo_tracker:
        #         a_link = jumbo_tracker.find_element(By.HTML, "a")
        #         restaurants[link].append(a_link.get_attribute("href"))
        #     else:
        #         print("No jumbo tracker")
        # except:
        #     print("No jumbo tracker")
        #     pass
    # break

print(restaurants)
print(len(restaurants))
# add to json file named zomato.json
with open('zomato.json', 'w') as f:
    json.dump(json.dumps(restaurants), f)

# - Created a web scraper using python and selenium to scrape data from zomato website.
# - The script is able to go to five different locations and scrape the data from the page.
# - Challenges:
#     - The page is dynamic and the data is loaded using lazy loading. We have to scroll down to load more data.
#     - The data is loaded in a grid format and we have to extract the data from each grid.
#     - The scraper needs to visit multiple pages and extract data from each page. This requires a lot of time
