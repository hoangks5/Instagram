from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle


# Check Login
def check_login(driver):
   try:
      driver.find_element_by_class_name('VMs3J')
      return 1
   except:
      return 0

# Login Instagram
def login(driver):
   driver = webdriver.Firefox()
   driver.set_window_size(width=360,height=1080)
   username = 'hoangkss5'
   passwd = 'Hoang22041999'
   if username not in open('./cookie/cookie.txt').read().splitlines():
      driver.get("https://www.instagram.com/accounts/login/")
      time.sleep(2)
      driver.find_element_by_name('username').send_keys(username)
      time.sleep(2)
      driver.find_element_by_name('password').send_keys(passwd)
      time.sleep(2)
      driver.find_element_by_name('password').send_keys(Keys.ENTER)
      time.sleep(5)
      driver.get(f"https://www.instagram.com/{username}")
      time.sleep(2)
      # Check Login Successful
      if check_login(driver=driver) == 0:
         return login(driver)
      read_cookie_file = open('./cookie/cookie.txt','r',encoding='utf-8').read().splitlines()
      read_cookie_file.append(username)
      string_read_cookie_file = '\n'.join(read_cookie_file)
      write_cookie_file = open('./cookie/cookie.txt','w',encoding='utf-8')
      write_cookie_file.write(string_read_cookie_file)
      write_cookie_file.close()
      pickle.dump( driver.get_cookies() , open(f"./cookie/{username}.pkl","wb"))

   else:
      driver.get(f"https://www.instagram.com/{username}")
      cookies = pickle.load(open(f"./cookie/{username}.pkl", "rb"))
      for cookie in cookies:
         driver.add_cookie(cookie)
      time.sleep(5)
      driver.refresh()
      time.sleep(2)
      # Check Login Successful
      if check_login(driver=driver) == 0:
         return login(driver)
      
login('driver')