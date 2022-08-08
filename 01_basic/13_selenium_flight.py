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
options.add_argument("--disable-dev-shm-usage") # /deb/shm 디렉토리 사용 안함, 로컬 PC의 메모리 사용

browser = webdriver.Chrome("chromedriver", options=options)
# browser.maximize_window() # 창 최대화


url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동
browser.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return [1, 2, 3, 4, 5]}})") # 위장 plugin 만들기
browser.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})") # 언어 설정
# screenshot()

# browser.find_element(By.CLASS_NAME, "tabContent_option__2y4c6.select_Date__1aF7Y").click()
browser.find_element(By.XPATH, "//*[contains(text(), '가는 날')]").click()
# screenshot()

# with open("source.html", "w", encoding="utf8") as f:
#     f.write(browser.page_source)

# # 이번달 27일, 28일 선택
browser.find_element(By.XPATH, "//*[contains(text(), '27')]").click()
browser.find_element(By.XPATH, "//*[contains(text(), '28')]").click()
# screenshot()

browser.quit()