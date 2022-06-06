#(new window.wordle.bundle.GameApp).solution


import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytextnow

import secrets


#set browser log
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = { 'browser':'ALL' }






client = pytextnow.Client(secrets.username, sid_cookie=secrets.connect_sid, csrf_cookie=secrets.csrf)


chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--auto-open-devtools-for-tabs")
chrome_options.add_argument('headless')



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome(desired_capabilities=dc, executable_path='C:/Users/Ayush/OneDrive/Documents/Code/chromedriver.exe', chrome_options=chrome_options, options=options)
driver.minimize_window()


driver.get('https://www.nytimes.com/games/wordle/index.html')

wordle_answer = driver.execute_script("return (new window.wordle.bundle.GameApp).solution")

time.sleep(1)


driver.close()



client.send_sms(secrets.number, "Wordle Today: " + wordle_answer)
