import requests
from bs4 import BeautifulSoup as BS
import webbrowser
from selenium import webdriver
import selenium
import os
from time import sleep
import re
acc = "https://iostudio.ru/?vk_access_token_settings=&vk_app_id=7125823&vk_are_notifications_enabled=0&vk_is_app_user=1&vk_is_favorite=0&vk_language=ru&vk_platform=desktop_web&vk_ref=other&vk_user_id=561977526&sign=q4GuMqeq44f8wsIWEfQ-6-76nbBh_b1biHH9F5YzddM#x=378.5&y=381"
r = requests.get ( acc )
soup = BS ( r.content , 'html.parser' )

#for q in soup.findAll('button', class_='btn btn-light updateCaptcha'):
    #print(q)

#webbrowser.open(acc, new=0, autoraise=True)
chromedriver = "./chromedriver"
#chromedriver = "/Users/geras_0v8j57t/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Chrome()
driver.get(acc)
sleep(2)
element = driver.find_element_by_css_selector('div#reloadGun')
element.click()
#element = driver.find_element_by_css_selector('button#catpchaButtonImage.btn.btn-light')



#print(captcha)

while True:
    element = driver.find_elements_by_css_selector('button.btn.btn-light.updateCaptcha')
    #print(elementt)
    captcha = driver.find_element_by_css_selector ( "button#catpchaButtonImage.btn.btn-light" ).get_attribute ("style" );
    captcha = captcha.replace('background-size: 20vh; background-position: center center; width: 100%; background-image: url("', '')
    captcha = captcha.replace('");', '')
    print(element)
    print(captcha)
    if element != []:
        element.click() #btn btn-light updateCaptcha btn-danger
        sleep(1)
        if driver.find_elements_by_css_selector ( "button.btn.btn-light.updateCaptcha.btn-danger" ) != []:
            sleep(11)
            #Записываем капчу
        else:
            element = driver.find_element_by_css_selector ( 'button.btn.btn-light.updateCaptcha' )
            element.click()
            #Выполняем капчу