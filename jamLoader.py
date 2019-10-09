from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
g = raw_input("Enter the vid you want to download.")
browser = webdriver.Firefox()
browser.get('https://youtubemultidownloader.net/')

elem = browser.find_element_by_id("inputUrl")
elem.send_keys(g+Keys.RETURN)
time.sleep(5)
try:
    elem3 = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[4]/div/div[2]/div[2]/div[1]/div[2]/a[1]")
    elem3.click()
except:
    print "Video is blocked."
    browser.close()
