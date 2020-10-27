####################################################################################################
#IMPORTS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import time
from bs4 import BeautifulSoup
import bs4
import requests
from urllib.request import urlopen as uReq
####################################################################################################

############## Webdrive
class Webdriver:
    #FUNCTIONS TO EXTRACT URL WITH CHROMEDRIVER AND BS4

    def __init__(self, arg1):
        self.url = arg1
        self.driver = self.create_webdriver()
        self.content = self.get_webdriver_content()
        self.soup = self.extract_bs4_from_web()
        self.quit_driver()


    def quit_driver(self):
        driver = self.driver    #do we need this?
        #### To quit the driver
        driver.quit()
        return()
    def extract_bs4_from_web(self):
        content = self.content  #do we need this?
        #### Parse the webdriver using html
        soup = BeautifulSoup(content,"html.parser")
        return(soup)
    def get_webdriver_content(self):
        driver = self.driver    #do we need this?
        #### Encode the webdriver page
        content = driver.page_source.encode('utf-8').strip()
        return(content)
    def create_webdriver(self):
        #### Create the webdriver given the url
        url = self.url      #do we need this?
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
        driver.maximize_window()
        driver.get(url)
        #to close the drive as soon as loaded (find a way to not open it at all)
        # time.sleep(0)
        return(driver)
