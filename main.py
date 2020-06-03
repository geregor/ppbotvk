import requests
from bs4 import BeautifulSoup as BS
import webbrowser
from selenium import webdriver
import os
acc = "https://iostudio.ru/?vk_access_token_settings=&vk_app_id=7125823&vk_are_notifications_enabled=0&vk_is_app_user=1&vk_is_favorite=0&vk_language=ru&vk_platform=desktop_web&vk_ref=other&vk_user_id=255117463&sign=_HR6bgZfXzqyylrACbDkaQY0IzvA--zyaMA142ch6tE#x=707.5&y=297"
r = requests.get ( acc )
soup = BS ( r.content , 'html.parser' )

#for q in soup.findAll('button', class_='btn btn-light updateCaptcha'):
    #print(q)

#webbrowser.open(acc, new=0, autoraise=True)

chromedriver = "/app/.heroku/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Chrome()
driver.get(acc)
element = driver.find_element_by_id('reloadGun')
element.click()
element = driver.find_element_by_css_selector('button.btn.btn-light.updateCaptcha')
element.click()
