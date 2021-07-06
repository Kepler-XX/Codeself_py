from time import sleep

from selenium import webdriver


url = "http://liuyan.people.com.cn/"

browser = webdriver.Chrome()
browser.get(url)
sleep(1)

browser.find_element_by_link_text("留言").click()
sleep(1)

browser.find_element_by_class_name("nav_active").click()
sleep(1)

browser.find_element_by_id("13").click()


browser.close()