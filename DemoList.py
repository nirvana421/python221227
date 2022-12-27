# DemoList.py
colors = ["red", "red", "green", "blue"]
print( colors )
print( type(colors) )
# 입력
colors.append( "white" )
print( colors )
colors.insert( 1, "yellow" )
colors += "red"
print( colors )
# 삭제
print( colors.pop() )
print( colors.pop() )
print( colors )

count = colors.count( "red" )
print( count )
print( "range: ", range(count) )
for i in range(count):
    colors.remove( "red" )
#colors.remove( "red" )
print( colors )

# set
a = {1,2,3,3}
b = {2,3,3,4}
print(a)
print(b)
print( a.union(b) )
print( a.intersection(b) )

# tuple
print( "-- tuple --" )
args = (2,3)
# 함수 정의
def times( a, b ):
    return a+b, a*b

print( times(*args) )
result = times( 3,4 )
print( result[0] )
print( result[1] )

print( "---형식변환--" )
a = set( (1,2,4) )
print( type(a) )
b = list(a)
b.append(4)
print( type(b) )
print( b )