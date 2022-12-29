# web1.py
# 웹에 데이터 수집하는 라이브러리
from bs4 import BeautifulSoup

# 웹 페이지 로딩 (함수나 메서드를 연속으로 부르는 메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
# 검색을 할 객체
soup = BeautifulSoup( page, "html.parser" )
# print( soup.prettify() )
# 문서 <p> 전부 검색
# print( soup.find_all("p") )
# print( soup.find("p") )
# 조건 <p class=outer-text>
# print( soup.find_all("p", class_="outer-text") )
# 내부 content만 출력
for item in soup.find_all("p"):
    title = item.text.strip()
    title = title.replace("\n", "")
    print(title)


