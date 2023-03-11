"""
Project) 웹 스크래핑을 이용하여 나만의 비서를 만드시오

[조건]
1. 네이버에서 오늘 서울의 날씨 정보를 가져온다.
2. 헤드라인 뉴스 3건을 가져온다.
3. IT 뉴스 3건을 가져온다.
4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다.

[출력 예시]

[오늘의 날씨]
흐림, 어제보다 00° 높아요
현재 00℃ (최저 00° / 최고 00°)
오전 강수확률 00% / 오후 강수확률 00%

미세먼지 00μg/m² 좋음
초미세먼지 00μg/m² 좋음

[헤드라인 뉴스]
1. 무슨 무슨 일이...
 (링크 : https://...)
2. 어떤 어떤 일이...
 (링크 : https://...)
3. 이런 저런 일이...
 (링크 : https://...)

[IT 뉴스]
1. 무슨 무슨 일이...
 (링크 : https://...)
2. 어떤 어떤 일이...
 (링크 : https://...)
3. 이런 저런 일이...
 (링크 : https://...)

[오늘의 영어 회화]
(영어 지문)
Jason : How do you think about bla bla..?
Kim : Well, I think ...

(한글 지문)
Jason : 어쩌구 저쩌구 어떻게 생각하세요?
Kim : 글쎄요, 저는 어쩌구 저쩌구


* 헤드라인 뉴스 -> 분야별 주요뉴스 로 변경
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def create_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920x1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    )
    options.add_argument("lang=ko_KR")
    # options.headless = True

    _browser = webdriver.Chrome("chromedriver", options=options)
    _browser.minimize_window()
    # browser.implicitly_wait(3)

    return _browser


def scrape_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    browser.get(url)

    summary = browser.find_element(By.CLASS_NAME, "summary").text.split("\n")
    weather = summary[2]  # 흐림
    temperature_diff = summary[0] + " " + summary[1]  # 어제보다 00° 높아요

    temperature = (
        browser.find_element(By.CLASS_NAME, "temperature_text").text.split("\n")[1].rstrip("°")
        + "℃"
    )  # 00℃

    temperature_range = browser.find_element(By.CLASS_NAME, "temperature_inner")
    lowest = temperature_range.find_element(By.CLASS_NAME, "lowest").text.split("\n")[1]  # 00°
    highest = temperature_range.find_element(By.CLASS_NAME, "highest").text.split("\n")[1]  # 00°

    rain = browser.find_element(By.CLASS_NAME, "cell_weather").text.split("\n")
    rain_poss = (rain[1], rain[4])  # 00%

    browser.find_element(By.CLASS_NAME, "today_chart_list").find_element(
        By.XPATH, "//*[text()='미세먼지']"
    ).click()
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "state_info._fine_dust._info_layer"))
    )

    fine_dust = browser.find_element(By.CLASS_NAME, "state_info._fine_dust._info_layer").text.split(
        "\n"
    )
    particulate1 = fine_dust[2].split(" ")
    ultrafine_dust = browser.find_element(
        By.CLASS_NAME, "state_info._ultrafine_dust._info_layer"
    ).text.split("\n")
    particulate2 = ultrafine_dust[2].split(" ")

    print("")
    print("[오늘의 날씨]")
    print(f"{weather}, {temperature_diff}")
    print(f"현재 {temperature}  (최저 {lowest} / 최고 {highest})")
    print(f"오전 강수확률 {rain_poss[0]} / 오후 강수확률 {rain_poss[1]}")
    print("")
    print(f"미세먼지 {particulate1[0]} μg/m² {particulate1[1]}")
    print(f"초미세먼지 {particulate2[0]} μg/m² {particulate2[1]}")
    print("")


def scrape_main_news():
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    browser.get(url)

    main_news = browser.find_elements(By.CLASS_NAME, "section")[1].find_elements(By.TAG_NAME, "a")

    print("[분야별 주요뉴스]")
    for i in range(3):
        print(f"{i + 1}. {main_news[i].text}")  # 1. 무슨 무슨 일이...
        print(f" (링크 : {main_news[i].get_dom_attribute('href')})")  # (링크 : https://...)
    print("")


def scrape_it_news():
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    browser.get(url)

    it_news = browser.find_element(By.CLASS_NAME, "list_body.section_index").find_elements(
        By.CLASS_NAME, "cluster_group._cluster_content"
    )

    print("[IT 뉴스]")
    for i in range(3):
        headline = (
            it_news[i].find_element(By.CLASS_NAME, "cluster_text").find_element(By.TAG_NAME, "a")
        )
        print(f"{i + 1}. {headline.text}")  # 1. 무슨 무슨 일이...
        print(f" (링크 : {headline.get_dom_attribute('href')})")  # (링크 : https://...)
    print("")


def scrape_english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    browser.get(url)

    english_convs = browser.find_elements(By.CLASS_NAME, "conv_txtBox")[1].find_elements(
        By.CLASS_NAME, "conv_sub"
    )
    korean_convs = browser.find_elements(By.CLASS_NAME, "conv_txtBox")[0].find_elements(
        By.CLASS_NAME, "conv_sub"
    )

    print("[오늘의 영어 회화]")
    print("(영어 지문)")
    for english_conv in english_convs:
        print(english_conv.text)
    print("")
    print("(한글 지문)")
    for korean_conv in korean_convs:
        print(korean_conv.text)


if __name__ == "__main__":
    browser = create_browser()

    scrape_weather()
    scrape_main_news()
    scrape_it_news()
    scrape_english()

    browser.quit()
