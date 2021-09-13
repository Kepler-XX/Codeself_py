from time import sleep

from selenium import webdriver


url = "http://liuyan.people.com.cn/"

browser = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver')
browser.get(url)
sleep(3)

browser.find_element_by_xpath("//li/a[contains(text(),'留言')]").click()
sleep(1)
browser.switch_to.window(browser.window_handles[-1])  # 窗口切换
browser.find_element_by_xpath("//li/a[contains(text(),'地方领导')]").click()
sleep(1)

browser.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/dl/div/a[1]").click()


# browser.close()