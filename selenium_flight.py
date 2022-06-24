from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "./chromedriver"
browser = webdriver.Chrome(driver_path)
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) 

# 가는 날 선택 클릭
brwoser.find_element_by_link_text("가는 날 선택").click()

# 이번달 27, 28일 선택
browser.find_element_by_link_text("27")[0].click() #[0] -> 이번달
browser.find_element_by_link_text("28")[0].click() #[0] -> 이번달

# 다음달 27, 28일 선택
# browser.find_element_by_link_text("27")[1].click() #[0] -> 다음달
# browser.find_element_by_link_text("28")[1].click() #[0] -> 다음달

# 제주도 선택