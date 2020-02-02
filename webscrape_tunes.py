# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:51:06 2020

@author: Home
"""



from selenium import webdriver
import os

#############################################################################
#
#                       Initialisation
#
#############################################################################

gecko = os.path.normpath(r'C:\Users\Home\Documents\Projects\download_certs\gecko_driver\geckodriver')
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')

# Set preferences: 
# 2 main things here are where to download, and to ensure that there are no
# user prompts while downloading.
fp = webdriver.FirefoxProfile()
# 0 means to download to the desktop
# 1 means to download to the default "Downloads" directory
# 2 means to use the directory 
#fp.set_preference("browser.download.folderList", 0)

import os
download_path = ("C:\\Users\\Home\\Desktop\\temp")

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.dir", download_path) 
fp.set_preference("browser.helperApps.alwaysAsk.force", False)
fp.set_preference("browser.download.manager.showWhenStarting",False)
# This the 'Content-Type' for the midi files:
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/midi");
#fp.set_preference("browser.download.dir", "H:\Downloads") 

# Launch the browser
driver = webdriver.Firefox(firefox_binary=binary,
                           executable_path=gecko+'.exe',
                           firefox_profile = fp)



#############################################################################
#
#                       Run the scraper
#
#############################################################################



url = 'https://thesession.org/tunes/2123'

scrape_page(driver = driver, url = url, directory = download_path)









