# function3.py
# 기본값이 있는 경우
def times( a=10, b=20 ):
    return a*b

# 호출
print( times() )
print( times(5) )
print( times(5,6) )

# 키워드 인자
def connectURI( server, port ):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print( connectURI("ycampus.com", "80") )
print( connectURI(port="80", server="ycampus.com") )

# 가변인자 (*는 tuple로 넘기는 경우)
def union(*args):
    result = []
    for item in args:
        for x in item:
            if x not in result:
                result.append(x)
    return result
# 호출
print( union("HAM", "EGG") )
print( union("HAM", "EGG", "SPAM") )

# 람다함수
g = lambda x, y : x*y
print( g(3,4) )
print( g(5,6) )
print( (lambda x:x*x)(3) )
print( globals() )