from selenium import webdriver
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
    sleep(5)

    # 获取登录按钮并点击
    login_but = browser.find_element_by_xpath('//button[contains(@class,"login-button")]')
    login_but.click()
    sleep(5)

    # 输入注册的账户 密码
    browser.find_element_by_xpath('//input[contains(@name,"mobileOrEmail")]').send_keys('15037241092')
    browser.find_element_by_xpath('//input[contains(@name,"password")]').send_keys('chaizhenhua.123')
    browser.find_element_by_xpath('//button[contains(@class,"sm-button submit")]').click()
    sleep(5)

    # 获取cookies
    cookies = browser.get_cookies()
    print(cookies)

except Exception as e:
    print('发生异常：',e)

finally:
    browser.close()