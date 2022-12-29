# web2.py

import urllib.request
# 크롤링
from bs4 import BeautifulSoup
f = open( "c:\\work\\webtoon.txt", "wt", encoding="utf-8" )

# 페이징 처리
for i in range(1,6):
    url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page={0}".format(i)
    print("url : ", url)
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser" )
    cartoons = soup.find_all( "td", class_="title" )
    for item in cartoons:
        title =  item.find("a").text.strip()
        print(title)
        f.write(title + "\n")

f.close()

# data = urllib.request.urlopen( 
#     "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri" )
# soup = BeautifulSoup(data, "html.parser" )

# cartoons = soup.find_all( "td", class_="title" )
# print( "갯수: {0}".format(len(cartoons)) )
# title = cartoons[0].find("a").text
# link = cartoons[0].find("a")["href"]
# print(title)
# print(link)

# # <td class="title">
# # 					<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.img','20853','50')">
# # 						<img src="https://shared-comic.pstatic.net/thumb/webtoon/20853/50/inst_thumbnail_20853_50.jpg" title="마음의 소리 50화 &lt;격렬한 나의 하루&gt;" alt="마음의 소리 50화 &lt;격렬한 나의 하루&gt;" width="71" height="41" onERROR="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/non71_41.gif'">
# # 						<span class="mask"></span>
# # 					</a>

# for item in cartoons:
#     title = item.find("a").text.strip()
#     print(title)