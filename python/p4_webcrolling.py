## 웹크롤링(Web Scrapping) : html에서 필요한 정보를 가져오는 것, 아래 3가지 방법
#1. urllib.request 모듈을 이용한 웹스크래핑
import urllib.request
import re #정규식모듈

url = "https://finance.naver.com/item/main.naver?code=005930"

html = urllib.request.urlopen(url) #urlopen으로 해당유알엘 내용 가져오기 
html_contents = str(html.read().decode("ms949")) # 한글이 깨짐을 방지하기 위해 decode 후 string으로 변환
# print(html_contents)
stock_result = re.findall("(<dl class=\"blind\">)([\\s\\S]+?)(</dl>)", html_contents) #백슬래시는 문자열 그대로 인식하도록 하기 위해 붙임. (패턴), []or, \s\S대소문자포함 +?여러개반복
# print(stock_result)
samsung_stock = stock_result[0]
# print(samsung_stock)
samsung_index = samsung_stock[1]
# print(samsung_index)
dd_result = re.findall("(\\<dd\\>)([\\s\\S]+?)(\\</dd\\>)", samsung_index)
# print(dd_result)
# for item in dd_result :
#     print(item[1])

#2. beautiful soup 이용, 설치: cmd에서 pip install bs4
from bs4 import BeautifulSoup #bs4 모듈에서 BeautifulSoup 함수만 임포트
import urllib.request as req #req란 이름으로 가져와라 

url2 = "https://finance.naver.com/marketindex/"
html2 = req.urlopen(url2)
html2 = html2.read().decode('cp949')
soup = BeautifulSoup(html2, "html.parser") #BeautifulSoup의 html.parser를 이용하면 손쉽게 개발가능
# print(soup)
price = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value") #개발자도구에 해당태그에 복사-selector복사로 가져옴 
# print("달러/원 = ", price)
price = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string #태그안에 문자열만 가져옴
# print("달러/엔 = ", price)

from bs4 import BeautifulSoup
import requests #외부모듈 설치 필요 cmd에서 pip install requests

url3 = "https://sports.news.naver.com/kbaseball/record/index?category=kbo"
response = requests.get(url3)
html3 = response.text
soup2 = BeautifulSoup(html3, "html.parser")
# print(soup2)
baseballList = soup2.select("#content > div.tb_kbo > div > div.tbl_box.p_head > table.pitcher > tbody > tr > td > div > ol > li.lead > a")
# print(baseballList)
# print(type(baseballList)) #<class 'bs4.element.ResultSet'> ResultSet는 집합모양 
# for rank, item in enumerate(baseballList, start=1) : #enumerate는 index를 붙여온다. start를 빼면 0부터 가져옴
#     print(rank, item.text)

## 셀레니움을 이용(동적데이타를 가져올때) 크롬 웹드라이브를 설치해야함 
from selenium import webdriver
import time
# 드라이브 지정
path = "./chromedriver.exe"
driver = webdriver.Chrome(path)

# 구글 사이트 검색
driver.get("http://www.google.com")
time.sleep(3)

search_box = driver.find_element_by_name('q')
search_box.send_keys("python")
search_box.submit()
time.sleep(5)

driver.close()




