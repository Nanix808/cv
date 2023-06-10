
import json
import bs4
import requests
import time
from datetime import datetime
import re
import xlsxwriter
import random
import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fake_useragent import UserAgent



def get_source_html():


    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    user_agent = UserAgent()

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36")
    # не закрывать браузер
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    url = r'https://www.linkedin.com/checkpoint/lg/sign-in-another-account'
    # url = 'https://www.httpbin.org/headers'

    browser = webdriver.Chrome(executable_path='backend\driver\chromedriver.exe',
                               options=options
    )

   
    try:
        browser.get(url)
        # time.sleep(5)
        email_input = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'username')))
        # email_input = browser.find_element(By.ID, 'username')
        email_input.clear()
        email_input.send_keys('####################')
        password_input = browser.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('###########')
        # time.sleep(2)
        submit_button = browser.find_element(By.CLASS_NAME, 'btn__primary--large')
        submit_button.click()
        # time.sleep(2)

        input_find = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-global-typeahead__input')))
        # input_find = browser.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
        input_find.send_keys('python')
        input_find.send_keys(Keys.ENTER)
        # print(input_find)

        time.sleep(20)
        


    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()

    # elem = browser.find_element(By.NAME, 'p')  # Find the search box
    # elem.send_keys('seleniumhq' + Keys.RETURN)

    # browser.quit()
 
    # url = 'https://rabota.by/search/vacancy?text=python&salary=&ored_clusters=true'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #     'Accept-Encoding': 'none',
    #     'Accept-Language': 'en-US,en;q=0.8',
    #     'Connection': 'keep-alive'}

    # response = requests.get(url=url, headers=headers)
   

    # soup = bs4.BeautifulSoup(response.text, "lxml")




    # print(soup)


if __name__ == '__main__':
    get_source_html()
    
