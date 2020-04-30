# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

from selenium import webdriver
from time import sleep
import pandas as pd
import numpy as np

class ryanair_bot:
    
    def __init__(self):
        chromedriver_path = '/Users/markkennedy/Documents/WebDriver/chromedriver'
        global driver 
        driver = webdriver.Chrome(executable_path=chromedriver_path)
        global sections_list 
        sections_list = []
        sleep(2)
    
    def page_scrape():
        xp_sections = '//*[@class="ff-list-item"]'
        sections = driver.find_elements_by_xpath(xp_sections)
        temp_sections_list = ([value.text for value in sections])
        temp_sections_list = [x.replace('in ', "") for x in temp_sections_list]
        temp_sections_list = ([value.split("\n") for value in temp_sections_list])
        sections_list.append(temp_sections_list)
        
    def load_next_page():
        next_page = '//div[contains(@class,"next vertical-center")]'
        driver.find_elements_by_xpath(next_page)[0].click()
        sleep(3)
        
    def check_next_page():
        next_prev_buttons = '//span [contains(@class,"nav-label")]'
        next_prev_buttons = driver.find_elements_by_xpath(next_prev_buttons)
        button_labels = [value.text for value in next_prev_buttons]
        next_button_label = 'Next'
        if next_button_label in button_labels:
            return True
        else:
            return False
        
    def create_df():
        sections_array = np.concatenate(sections_list, axis=0 )
        columns = ["City", "Country", "Month", "Price", "Ticket"]
        global df
        df = pd.DataFrame(data=sections_array, columns=columns)
        print(df)
        
    def start_ryanair(self,airport, departure_date, return_date, budget):
        ryanair = ('https://www.ryanair.com/ie/en/cheap-flights/?from=' + airport + '&out-from-date=' + departure_date + '&out-to-date=' + departure_date + '&in-from-date=' + return_date + '&in-to-date=' + return_date + '&budget=' + budget)
        driver.get(ryanair)
        sleep(60)
        while True:
            ryanair_bot.page_scrape()
            if ryanair_bot.check_next_page() == False:
                break
            else:
                ryanair_bot.load_next_page()
        driver.close()
        return ryanair_bot.create_df()
        
        