# demoDict.py
devices = {"아이폰":5, "아이패트":10, "윈도우태블릿":15}
print( type(devices) )
print( devices )
# 검색
print( "%s: %s" % ("아이패트", devices["아이패트"]) )

# 입력
devices["맥북"] = 20
print( devices )

devices["아이폰"] = 6
print( devices )
#삭제
del devices["아이폰"]
print( devices )

# 참조만 복사, call by reference
print( "--- Call by Reference ---" )
devices2 = devices
devices2["에어팟"] = 3
print(devices)
print(devices2)
print( id(devices), id(devices2) )

print( "--- Items ---" )
for item in devices.items():
    print(item)

print("--- Keys ---")
for item in devices.keys():
    print(item)

print("--- Values ---")
for item in devices.values():
    print(item)

print( "---- Bool ------" )
print( "bool(0) : ", bool(0) )
print( "bool(\"\"): ", bool("") )
print( "bool([]): ", bool([]) )
print( "bool([3]): ", bool([3]) )
print( "bool(\"test\"): ", bool("test") )
isRight = True
print( type(isRight) )
print( "1<2 : ", 1<2 )
print( "1 != 2 : ",  1 != 2 )

print( "--- 나누기 ---" )
print( 5/2 )
print( 5//2 )
print( 5%2 )
