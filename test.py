from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle
driver = webdriver.Firefox()
""" driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
driver.find_element_by_name('username').send_keys('hoangks5')
time.sleep(2)
driver.find_element_by_name('password').send_keys('Hoang22041999')
time.sleep(2)
driver.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(5) """
driver.get("https://www.instagram.com/hoangks5")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
   driver.add_cookie(cookie)
time.sleep(5)
driver.refresh()