# demoRE.py
# 정규표현식 (특정 패턴, 규칙 찾기)
import re

# 처음부터 끝가지 지독하게 패턴 검색
result =  re.search( "[0-9]*th", "   35th")
# 매칭 오브젝트(문자열이 아님)
print(result)
print( result.group() )

# result = re.match( "[0-9]*th", "   35th" )
# print( result )
# print( result.group() )

result = re.search( "apple", "this is an Apple".lower() )
print( result.group() )
result = re.search( "\d{4}", "올해는 2022년입니다.")
print( result.group() )

result = re.search( "\d{5}", "우리 동네 우편번호는 60779")
print( result.group() )

print( "--- 다중라인 ---" )
s = """이 문자열은
다음과 같이 

빈둘도 있고, 다중 라인입니다."""
# 시작할 때 .글자하나 +는 하나 이상
c = re.compile("^.+", re.M)
print( c.findall(s) )