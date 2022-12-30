# DemoForm2.py
# DemoForm.ui (화면단) + DemoForm.py (로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import urllib.request
# 크롤링
from bs4 import BeautifulSoup

#화면 로딩
form_class = uic.loadUiType( "DemoForm2.ui" )[0]

#폼 클래스(윈도우 정의)
class DemoForm( QMainWindow, form_class ):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("두번째 QT데모~")
    def clickFirstButton(self):
        # 파일로 저장
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
        self.label.setText("네이버 웹툰 크롤링 종료~")

    def clickSecondButton(self):
        self.label.setText("두번째 버튼~")
    def clickThirdButton(self):
        self.label.setText("세번째 버튼~")

# 진입점 체크
if __name__ == "__main__":
    # 실행 프로세스 생성
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    # 화면 출력
    demoWindow.show()
    # 이벤트 처리 대기(실행중)
    app.exec()
