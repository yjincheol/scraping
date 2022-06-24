#pip install selenium
#web driver check - chrome://version = 102.0.5005.115
#chrome driver download - https://chromedriver.chromium.org/downloads

from selenium import webdriver
import time

driver_path = "./chromedriver"
browser = webdriver.Chrome(driver_path)

#1. 네이버 이동
url = "https:naver.com"
browser.get(url) 

#2. 네이버 로그인 
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. id, password 입력
browser.find_element_by_id("id").send_keys("naverID")
browser.find_element_by_id("pw").send_keys("password")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

#5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_ID")

#6. html 정보 출력
print(browser.page_source)

#7. 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료