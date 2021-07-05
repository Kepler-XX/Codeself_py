from time import sleep

from selenium import webdriver


url = "http://liuyan.people.com.cn/"

browser = webdriver.Chrome()
browser.get(url)

sleep(3)
browser.find_element_by_class_name("fl")

browser.close()