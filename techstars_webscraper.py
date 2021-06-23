# Filters no accel https://www.techstars.com/portfolio?industries=Artificial+Intelligence+%26+Machine+Learning
# &industries=Biotech&industries=Blockchain+%26+Cryptocurrency&industries=Cleantech&industries=Cybersecurity
# &industries=Developer+Tools&industries=Fintech&industries=Future+of+Work&industries=Gaming&industries=Govtech+%26
# +Regtech&industries=Health+%26+Wellness&industries=Healthcare+%28hardware%29&industries=Healthcare+%28software%29
# &industries=Life+Sciences&industries=Pharma&industries=Robotics&industries=SaaS&industries=Smart+Cities&industries
# =Technology&industries=VR+%26+AR&status=Operating


import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import scrapy
import time
import csv

'''
TO DO! 
- MAKE LIST OF THINGS WITH FOUNDERS CSS AND SEARCH FOR FOUNDERS KEY WORD TO GET ACCURATE FOUNDER INFO
- FIX 1ST COMPANY ISSUE, 1ST AND SECOND COMPANY IS BEING CLICKED, ALSO DO THIS ^ 
- TEST DATE FIX
'''


class Company:
    def __init__(self, name, founder, linkedin, website, description, location, date):
        self.name = name
        self.founder = founder
        self.linkedin = linkedin
        self.website = website
        self.description = description
        self.location = location
        self.date = date



names = []
founders = []
linkedins = []
websites = []
descriptions = []
locations = []
dates = []

def isoDate(date_text):
    date_num = date_text.find("20")
    date_text_striped = date_text[date_num:date_num + 4]
    return date_text_striped


# you have to download a web driver for this to work (I used chrome)
'''put your driver path here!!'''
driver_path = "/Users/tyarpornsuksant/Downloads/chromedriver"
driver = webdriver.Chrome(driver_path)

'''put your url here!!'''
# directory_url = "https://www.techstars.com/portfolio?industries=Artificial+Intelligence+%26+Machine+Learning&industries=Biotech&industries=Blockchain+%26+Cryptocurrency&industries=Cleantech&industries=Cybersecurity&industries=Developer+Tools&industries=Fintech&industries=Future+of+Work&industries=Gaming&industries=Govtech+%26+Regtech&industries=Health+%26+Wellness&industries=Healthcare+%28hardware%29&industries=Healthcare+%28software%29&industries=Life+Sciences&industries=Pharma&industries=Robotics&industries=SaaS&industries=Smart+Cities&industries=Technology&industries=VR+%26+AR&status=Operating"
directory_url ="https://www.techstars.com/portfolio?industries=Artificial+Intelligence+%26+Machine+Learning&industries=Biotech&industries=Blockchain+%26+Cryptocurrency&industries=Cleantech&industries=Cybersecurity&industries=Developer+Tools&industries=Fintech&industries=Future+of+Work&industries=Gaming&industries=Govtech+%26+Regtech&industries=Health+%26+Wellness&industries=Healthcare+%28hardware%29&industries=Healthcare+%28software%29&industries=Life+Sciences&industries=Pharma&industries=Robotics&industries=SaaS&industries=Smart+Cities&industries=Technology&industries=VR+%26+AR&status=Operating&currentPage=2"
driver.get(directory_url)

page_number = 1
max_pages = 6
while page_number <= max_pages:
    curr_names = []
    if page_number == 1:
        directory_url = "https://www.techstars.com/portfolio?industries=Artificial+Intelligence+%26+Machine+Learning&industries=Biotech&industries=Blockchain+%26+Cryptocurrency&industries=Cleantech&industries=Cybersecurity&industries=Developer+Tools&industries=Fintech&industries=Future+of+Work&industries=Gaming&industries=Govtech+%26+Regtech&industries=Health+%26+Wellness&industries=Healthcare+%28hardware%29&industries=Healthcare+%28software%29&industries=Life+Sciences&industries=Pharma&industries=Robotics&industries=SaaS&industries=Smart+Cities&industries=Technology&industries=VR+%26+AR&status=Operating"
    else:
        directory_url = "https://www.techstars.com/portfolio?industries=Artificial+Intelligence+%26+Machine+Learning&industries=Biotech&industries=Blockchain+%26+Cryptocurrency&industries=Cleantech&industries=Cybersecurity&industries=Developer+Tools&industries=Fintech&industries=Future+of+Work&industries=Gaming&industries=Govtech+%26+Regtech&industries=Health+%26+Wellness&industries=Healthcare+%28hardware%29&industries=Healthcare+%28software%29&industries=Life+Sciences&industries=Pharma&industries=Robotics&industries=SaaS&industries=Smart+Cities&industries=Technology&industries=VR+%26+AR&status=Operating" + "&currentPage= " + str(page_number)
    driver.get(directory_url)
    time.sleep(5)  # for page to load
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    # print(soup)
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)
    try:
        companies_test = soup.find_all('div', class_="CompanyCard")
    except:
        print("cards not found")
        break
    for company_html in companies_test:
        name = company_html.find('span', class_="jss1464")
        print(name.text)
        names.append(name.text)
        curr_names.append(name.text)
        try:
            location = company_html.find('span', class_="jss1465")
            print(location.text)
            locations.append(location.text)
        except:
            locations.append("None")
        try:
            description = company_html.find('p', class_="jss1467")
            print(description.text)
            descriptions.append(description.text)
        except:
            descriptions.append("None")
        try:
            date = company_html.find('p', class_="jss1466")  # put in func
            date_striped = isoDate(date.text)
            print(date_striped)
            dates.append(date_striped)
        except:
            dates.append("None")
        print(curr_names)
    for n in curr_names:
        try:
            clickable = driver.find_element_by_xpath('//*[@id="' + n + '"]')
            action = webdriver.common.action_chains.ActionChains(driver)
            action.move_to_element_with_offset(clickable, 1, 1)
            action.click()
            action.perform()
            print("I just clicked: " + '//*[@id="' + n + '"]')
            time.sleep(5) # take out?
            print(n + " was found")
        except:
            print("clickable not found")

        company_page_source = driver.page_source
        company_soup = BeautifulSoup(company_page_source, 'html.parser')
        # in company profile now!
        try:
            founder = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div/div/div/div[3]/div[1]/div[3]/a/p")
            print(founder.text)
            founders.append(founder.text)
        except:
            print("Founder not found")
            founders.append("None")
        try:
            linkedin = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div/div/div/div[3]/div[1]/div[3]/a[1]")
            print(linkedin.get_attribute('href'))
            linkedins.append(linkedin.get_attribute('href'))
        except:
            print("linkedin not found")
            linkedins.append("None")
        try:
            website = company_soup.find('a', class_="jss783")
            print(website['href'])
            websites.append(website['href'])
        except:
            print("website not found")
            websites.append("None")
        try:
            close_button = driver.find_element_by_class_name("jss776")
            close_button.click()
        except:
            print("button not found")
    page_number += 1


    # click next
    # try:
    #     driver.execute_script("window.scrollBy(0,500)")
    #     driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[7]/button').click()
    #     time.sleep(2)
    # except:
    #     break

print(names)
print(founders)
print(linkedins)
print(websites)
print(descriptions)
print(locations)
print(dates)


companies = []
for r in range(len(names)):
    companies.append(Company(names[r], founders[r], linkedins[r], websites[r],descriptions[r], locations[r], dates[r]))

with open('techstarsinfo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["title", "location", "founder", "description", "linkedin", "website"])
    for company in companies:
            try:
                if company.date == '2020' or company.date == '2021':
                    writer.writerow([company.name, company.founder, company.linkedin, company.website, company.description, company.location])
                    print(company.name + " was recorded")
                else:
                    print((company.name + " was deemed outdated with date " + company.date))
            except:
                print("There was something wrong with " + company.name + ". It could not be recorded")
# # Testing
# time.sleep(5)  # for page to load
# source = driver.page_source
# soup = BeautifulSoup(source, 'html.parser')
# # print(soup)
# driver.execute_script("window.scrollTo(0, 500)")
# time.sleep(3)
# try:
#     while True:
#         driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[7]/button').click()
#         time.sleep(3)
#         print("I worked!")
# except:
#     print("I failed")
#
