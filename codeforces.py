from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://codeforces.com/enter?back=%2F')
time.sleep(10)
elem = browser.find_element_by_id("handleOrEmail")
elem.send_keys("mah_name_boiii")
elem2 = browser.find_element_by_id("password")
elem2.send_keys("password")
elem3 = browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[4]/td/div[1]/input")
elem3.click()
