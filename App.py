from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.chrome("chromedriver")
browser.get(start_url)
time.sleep(10)

def Scrap():
    headers = ["Name","Distance","Mass","Radius"]
    planet_data = []
    for i in range(0,98):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attr={'class','wikitable sortable jquery-tablesorter'}):
            li_tag = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tag):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
                planet_data.append(temp_list)
    browser.find_element_buy_xpath('//*[@id="mw-content-text"]/div[1]/table/thead/tr/th[3]/a').click()   
    
    with open("scrapper_2.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(planet_data) 

Scrap()