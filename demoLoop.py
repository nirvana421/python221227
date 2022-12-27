# demoLoop.py
# 다중라인 주석처러 : ctrl + /

# score = int( input("점수 입력하세요: ") )
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# elif 60 <= score < 70:
#     grade = "D"
# else:
#     grade = "F"

# print( "등급은 ", grade )

# value = 5
# while value > 0:
#     print(value)
#     value -= 1

# d = {"apple": 100, "orange":200, "banana":300}
# for item in d.items():
#     print(item)
# print( "--- break ----" )
# lst = range(1,11)
# for i in lst:
#     if i>5:
#         break
#     print( "item:{0}".format(i))

# print( "--- continue ---" )
# for i in lst:
#     if i % 2 == 0:
#         continue
#     print( "item:{0}".format(i))

print("--- 수열 함수 ---")
print( list(range(10)) )
print( list(range(2000, 2023)) )
print( list(range(1,32)) )

print( "--- 리스트 내장---" )
lst =  list(range(1,11))
print( [i**2 for i in lst if i > 5])

d = {100:"apple", 200:"banana", 300:"kiwi"}
print( [v.upper() for v in d.values()])

print("--- 필터 함수 이용 ---")
lst = [19, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

# 함수 정의
print("--- 필터링 함수 정의---")
def getBiggerThan20(i):
    return i>20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("--- lambda 함수 ---")
iterL = filter(lambda i:i>20, lst)
for item in iterL:
    print(item)
