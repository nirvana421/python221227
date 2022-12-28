# -*- 생성자와 소멸자 -*-
class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instance is created! value = ", value)
    def __del__(self):
        print("Instance is deleted!")


d = MyClass(10)
#del d

print( "전체 코드 실행 종료" )

