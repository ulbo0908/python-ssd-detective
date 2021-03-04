import os
from time import sleep #지정한 초만큼 여유를 주는 것
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
from private import private

driver_path = r"C:\Users\유정\Workspace\chromedriver_win32"
driver_name = "chromedriver.exe"
driver_path = os.path.join(driver_path,driver_name)
driver = webdriver.Chrome(driver_path)
base_url = "https://www.naver.com/"
login_url = "https://nid.naver.com/nidlogin.login"
driver.get(login_url)
sleep(1)

my_id = "ulbo0908"
my_pw = ""
naver_id = driver.find_element_by_id("id")
naver_pw = driver.find_element_by_id("pw")
sleep(1)

naver_id.click()
pyperclip.copy(my_id)
naver_id.send_keys(Keys.CONTROL, 'v')
sleep(1)
naver_pw.click()
pyperclip.copy(my_pw)
naver_pw.send_keys(Keys.CONTROL, 'v')
sleep(1)

driver.find_element_by_id("log.login").click()
sleep(2)

news_urls = {
    "조선일보" : "https://news.naver.com/main/ranking/office.nhn?officeId=023",
    "한겨레" : "https://news.naver.com/main/ranking/office.nhn?officeId=028"
}

driver.get(news_urls["조선일보"])

#news_list = driver.find_element_by_class_name("rankingnews_list")
#print(news_list.get_attribute('innerHTML'))