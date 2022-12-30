# DemoForm.py
# DemoForm.ui (화면단) + DemoForm.py (로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#화면 로딩
form_class = uic.loadUiType( "DemoForm.ui" )[0]

#폼 클래스(윈도우 정의)
class DemoForm( QDialog, form_class ):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 QT데모")

# 진입점 체크
if __name__ == "__main__":
    # 실행 프로세스 생성
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    # 화면 출력
    demoWindow.show()
    # 이벤트 처리 대기(실행중)
    app.exec()
