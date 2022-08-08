from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def screenshot():
    browser.get_screenshot_as_file(f"screenshot{screenshot.num}.png")
    screenshot.num += 1
screenshot.num = 1

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15")
options.add_argument("lang=ko_KR")
options.add_argument("--disable-dev-shm-usage") # /deb/shm 디렉토리 사용 안함, 로컬 PC의 메모리 사용

browser = webdriver.Chrome("chromedriver", options=options)
browser.maximize_window() # 창 최대화


url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동
browser.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return [1, 2, 3, 4, 5]}})") # 위장 plugin 만들기
browser.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})") # 언어 설정
# screenshot()

# browser.find_element(By.CLASS_NAME, "tabContent_option__2y4c6.select_Date__1aF7Y").click()
browser.find_element(By.XPATH, "//button[text()='가는 날']").click()
# screenshot()

# with open("source.html", "w", encoding="utf8") as f:
#     f.write(browser.page_source)

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//b[text()='27']")))
# stale element reference: element is not attached to the page document -> 너무 빠르게 명령어를 실행함

# 이번달 27일, 다음달 28일 선택
browser.find_elements(By.XPATH, "//b[text()='27']")[0].click()
browser.find_elements(By.XPATH, "//b[text()='28']")[1].click()
# screenshot()

browser.find_element(By.XPATH, "//b[text()='도착']").click()
browser.find_element(By.XPATH, "//*[contains(@placeholder, '국가')]").send_keys("제주")
browser.find_element(By.XPATH, "//*[text()='제주국제공항']").click()

browser.find_element(By.XPATH, "//*[text()='항공권 검색']").click()
