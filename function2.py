# function2.py
print( "--- 불변형식 ---" )
a = 1.3
print( id(a) )
a = 2.3
print( id(a) )

print( "--- 가변형식 ---" )
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

print( "--- 입력+출력 ---" )
def change(x):
    x2 = x[:]
    x2[0] = "H"
    print( "함수내 : ", x2)

def change2(x):
    x[0] = "H"

wordlist = ["J", "A", "M"]
print( "호출전 : ", wordlist )
change( wordlist )
print( "호출후 : ", wordlist)

# 리스트가 아닌 경우 Deep copy할 때
import copy

lst = [100,200,300]
lst2 = copy.deepcopy(lst)
lst2[0] = 101
print(lst)
print(lst2)
print( id(lst), id(lst2) )

# 함수내부의 이름 해석 순서 (LGB: local, global, built-in)
# global
x = 5
def func(a):
    return x+a
print( func(1) )

def func2(a):
    x=10
    return x+a
print( func2(1) )
