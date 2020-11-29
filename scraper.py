from bs4 import BeautifulSoup
import urllib.request as urllib2
from selenium import webdriver
import regex as re
import time
import pprint
import random
import csv

def get_listing(url):
    print(type(url),' ' ,url)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    time.sleep(30)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage = document.body.height;return lenOfPage;")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    page_content = soup.text
    page_content = re.sub(r'([a-z]|[0-9])([A-Z])', r'\1 \2', page_content)
    return page_content
    