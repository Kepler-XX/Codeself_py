from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

option = Options()


# 无头模式
option.add_argument('--headless')
option.add_argument('--disable-gpu')

# 规避检测（去掉webdriver）
# 1.chrome版本号小于88
"""
web = Chrome()
web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
 "source":'''
  window.navigator.webdriver = undefined
    Object.defineProperty(navigator, 'webdriver',{
    get: () ==> undefined
    })
 })
web.get("xxxx")
"""
# 2 chrome版本号大于88
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')


web = Chrome(options=option)
# web = Chrome()


# 打开网站
web.get('xxxx')
# 根据xpath定位网页某元素
web.find_element_by_xpath('xxx')