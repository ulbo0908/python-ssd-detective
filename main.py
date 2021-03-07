import os
from time import sleep #지정한 초만큼 여유를 주는 것
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
# from private import private

driver_path = r"C:\Users\유정\Workspace\chromedriver_win32"
driver_name = "chromedriver.exe"
driver_path = os.path.join(driver_path,driver_name)
driver = webdriver.Chrome(driver_path)
base_url = "https://www.naver.com/"
# login_url = "https://nid.naver.com/nidlogin.login"
# driver.get(login_url)
# sleep(1)

# my_id = private["id"]
# my_pw = private["pw"]
# naver_id = driver.find_element_by_id("id")
# naver_pw = driver.find_element_by_id("pw")
# sleep(1)

# naver_id.click()
# pyperclip.copy(my_id)
# naver_id.send_keys(Keys.CONTROL, 'v')
# sleep(1)
# naver_pw.click()
# pyperclip.copy(my_pw)
# naver_pw.send_keys(Keys.CONTROL, 'v')
# sleep(1)

# driver.find_element_by_id("log.login").click()
# sleep(2)

news_urls = {
    "조선일보" : "https://news.naver.com/main/ranking/office.nhn?officeId=023",
    "한겨레" : "https://news.naver.com/main/ranking/office.nhn?officeId=028"
}

driver.get(news_urls["조선일보"])

news_list_box = driver.find_elements_by_class_name("rankingnews_list")[1]
news_lists = news_list_box.find_elements_by_tag_name("li")
top_rank_news = news_lists[0]

top_rank_news.find_element_by_tag_name("a").click()

driver.find_element_by_id("articleTitleCommentCount").click()
sleep(2)

# while True:
#     try:
#         driver.find_element_by_class_name("u_cbox_page_more").click()
#         sleep(0.2)
#     except:
#         break

cboxes = driver.find_elements_by_class_name("u_cbox_comment_box")
print(len(cboxes))
cbox = cboxes[0]
print(cbox.text)

nickname = driver.find_element_by_class_name("u_cbox_nick")
print(nickname.text)

date = driver.find_element_by_class_name("u_cbox_date")
print(date.text)

comment = driver.find_element_by_class_name("u_cbox_contents")
print(comment.text)

like = driver.find_element_by_class_name("u_cbox_cnt_recomm")
print(like.text)

dislike = driver.find_element_by_class_name("u_cbox_cnt_unrecomm")
print(dislike.text)