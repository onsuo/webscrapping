import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
)
options.add_argument("lang=ko_KR")
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--disable-dev-shm-usage") # /deb/shm 디렉토리 사용 안함, 로컬 PC의 메모리 사용

browser = webdriver.Chrome("chromedriver", options=options)
# 창 최대화
browser.maximize_window()

url = "https://flight.naver.com/flights/"
# url 로 이동
browser.get(url)
# 위장 plugin 만들기
browser.execute_script(
    "Object.defineProperty(navigator, 'plugins', {get: function() {return [1, 2, 3, 4, 5]}})"
)
# 언어 설정
browser.execute_script(
    "Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})"
)

# browser.find_element(By.CLASS_NAME, "tabContent_option__2y4c6.select_Date__1aF7Y").click()
browser.find_element(By.XPATH, "//button[text()='가는 날']").click()

# 다음달 27일, 다다음달 28일 선택
# stale element reference: element is not attached to the page document -> 너무 빠르게 명령어를 실행함
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//b[text()='27']")))
browser.find_elements(By.XPATH, "//b[text()='27']")[1].click()
time.sleep(1)
browser.find_elements(By.XPATH, "//b[text()='28']")[2].click()


time.sleep(1)
browser.find_element(By.XPATH, "//b[text()='도착']").click()
time.sleep(1)
browser.find_element(By.XPATH, "//*[contains(@placeholder, '국가')]").send_keys("제주")

time.sleep(1)
browser.find_element(By.XPATH, "//*[text()='제주']").click()

time.sleep(1)
browser.find_element(By.XPATH, "//*[text()='항공권 검색']").click()

try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "domestic_schedule__1Whiq"))
    )
    print(elem.text)
finally:
    browser.close()
