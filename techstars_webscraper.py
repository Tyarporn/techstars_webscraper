# Filters no accel https://www.techstars.com/portfolio?industries=Artificial+Intelligence+%26+Machine+Learning
# &industries=Biotech&industries=Blockchain+%26+Cryptocurrency&industries=Cleantech&industries=Cybersecurity
# &industries=Developer+Tools&industries=Fintech&industries=Future+of+Work&industries=Gaming&industries=Govtech+%26
# +Regtech&industries=Health+%26+Wellness&industries=Healthcare+%28hardware%29&industries=Healthcare+%28software%29
# &industries=Life+Sciences&industries=Pharma&industries=Robotics&industries=SaaS&industries=Smart+Cities&industries
# =Technology&industries=VR+%26+AR&status=Operating


import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import scrapy
import time
import csv

'''TO DO! CLICK NEXT BUTTON, SCROLL TO BOTTOM OF PAGE?'''


class Company:
    def __init__(self, name, founder, linkedin, website, description, location, date):
        self.name = name
        self.founder = founder
        self.linkedin = linkedin
        self.website = website
        self.description = description
        self.location = location
        self.date = date


companies = []


def isoDate(date_text):
    date_num = date_text.find("20")
    date_text_striped = date_text[date_num:date_num + 4]
    return date_text_striped


# you have to download a web driver for this to work (I used chrome)
'''put your driver path here!!'''
driver_path = "/Users/tyarpornsuksant/Downloads/chromedriver"
driver = webdriver.Chrome(driver_path)

'''put your url here!!'''
directory_url = "https://www.techstars.com/portfolio?industries=Artificial+Intelligence+%26+Machine+Learning&industries=Biotech&industries=Blockchain+%26+Cryptocurrency&industries=Cleantech&industries=Cybersecurity&industries=Developer+Tools&industries=Fintech&industries=Future+of+Work&industries=Gaming&industries=Govtech+%26+Regtech&industries=Health+%26+Wellness&industries=Healthcare+%28hardware%29&industries=Healthcare+%28software%29&industries=Life+Sciences&industries=Pharma&industries=Robotics&industries=SaaS&industries=Smart+Cities&industries=Technology&industries=VR+%26+AR&status=Operating"
driver.get(directory_url)

time.sleep(5)  # for page to load
source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
# print(soup)

# find company data from overlay
try:
    names = []
    founders = []
    linkedins = []
    websites = []
    descriptions = []
    locations = []
    dates = []
    companies_test = soup.find_all('div', class_="CompanyCard")
    for company_html in companies_test:
        name = company_html.find('span', class_="jss1464")
        print(name.text)
        names.append(name.text)
        location = company_html.find('span', class_="jss1465")
        print(location.text)
        locations.append(location.text)
        description = company_html.find('p', class_="jss1467")
        print(description.text)
        descriptions.append(description.text)
        date = company_html.find('p', class_="jss1466")  # put in func
        date_striped = isoDate(date.text)
        print(date_striped)
        dates.append(date_striped)
    try:
        for n in names:
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="' + n + '"]').click()
            time.sleep(5)
            print(n + " was found")
            company_page_source = driver.page_source
            # if n == "askneo.io":
            #     print(company_page_source)
            company_soup = BeautifulSoup(company_page_source, 'html.parser')
            # in company profile now!
            try:
                founder = driver.find_element_by_xpath(
                    "/html/body/div[2]/div[3]/div/div/div/div/div/div[3]/div[1]/div[3]/a/p")
                print(founder.text)
                founders.append(founder.text)
            except:
                print("Founder not found")
                founders.append(" ")
            try:
                linkedin = driver.find_element_by_xpath(
                    "/html/body/div[2]/div[3]/div/div/div/div/div/div[3]/div[1]/div[3]/a[1]")
                print(linkedin.get_attribute('href'))
                linkedins.append(linkedin.get_attribute('href'))
            except:
                print("linkedin not found")
                linkedins.append(" ")
            try:
                website = company_soup.find('a', class_="jss783")
                print(website['href'])
                websites.append(website['href'])
            except:
                print("website not found")
                websites.append(" ")

            close_button = driver.find_element_by_class_name("jss776")
            close_button.click()

    except:
        print("button not found")

except:
    print("cards not found")

# click button next?

print(names)
print(founders)
print(linkedins)
print(websites)
print(descriptions)
print(locations)
print(dates)
