from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

# -----------------------------------------------------WEB SCRAPING WITH BEAUTIFULSOUP------------------------------#


response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

all_links = soup.select(".StyledPropertyCardPhotoBody a")
link_list = []
for link in all_links:
    link_list.append(link.get("href"))

all_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = []
for price in all_prices:
    prices.append(price.string[0:6])

all_addresses = soup.select("a address")
addresses = []
for add in all_addresses:
    addresses.append(add.string.strip().replace('|', ''))

# ------------------------------------------------DATA ENTRY USING SELENIUM-------------------------------------#

keys = Keys()
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_option)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSePIj-OxiiT18edqvJ75c0TDVYQ2Us_hwYbVOmsKnqQ1TwAww/viewform")

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSePIj-OxiiT18edqvJ75c0TDVYQ2Us_hwYbVOmsKnqQ1TwAww/viewform")
    time.sleep(2)

    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(link_list[n])
    submit_button.click()

driver.quit()
