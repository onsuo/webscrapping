from selenium import webdriver
from selenium.webdriver.common.by import By

def screenshot():
    browser.get_screenshot_as_file(f"screenshot{screenshot.num}.png")
    screenshot.num += 1
screenshot.num = 1

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15")
options.add_argument("lang=ko_KR")

browser = webdriver.Chrome("chromedriver", options=options)
# browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동
screenshot()

browser.find_element(By.LINK_TEXT, "가는날 선택").click()
screenshot()

# 이번달 27일, 28일 선택
browser.find_elements(By.LINK_TEXT, "27")[0].click()
browser.find_elements(By.LINK_TEXT, "28")[0].click()
screenshot()

browser.quit()
