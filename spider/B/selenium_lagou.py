from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep


web = Chrome()

web.get('https://www.lagou.com')
sleep(1)
web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[9]/a').click()
sleep(1)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
sleep(1)
web.find_element_by_xpath('//*[@id="order"]/li/div[1]/a[2]').click()

web.close()