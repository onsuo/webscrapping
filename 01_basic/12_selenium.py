import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def screenshot():
    browser.get_screenshot_as_file(f"screenshot{screenshot.num}.png")
    screenshot.num += 1
screenshot.num = 1

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_argument("use-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15")

browser = webdriver.Chrome("chromedriver", options=options)

# 1. 네이버로 이동
browser.get("https://naver.com")
screenshot()

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()
screenshot()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("password")
screenshot()

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()
screenshot()

time.sleep(3)

# 5. id 를 새로 입력
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")
screenshot()

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 브라우저 전체 종료
