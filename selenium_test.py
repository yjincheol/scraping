#pip install selenium
#web driver check - chrome://version = 102.0.5005.115
#chrome driver download - https://chromedriver.chromium.org/downloads

from selenium import webdriver
path = "./chromedriver"
browser = webdriver.Chrome(path)
browser.get("https:naver.com") 