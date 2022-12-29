# db1.py
import sqlite3

# 1) db 연결
# con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\work\\sample.db")
# 2) 커서객체 (실제 SQL 구문을 실행하고 결과 다룸)
cur = con.cursor()
# 테이블 생성
cur.execute( "create table PhoneBook (name text, phonenum text);")
# 1건 입력
cur.execute( "insert into PhoneBook values ('derick', '010-123-1234');")

name = "jinsoo"
phoneNum = "010-123-1234"
cur.execute( "insert into PhoneBook values (?, ?);", (name, phoneNum))

# 여러 건 입력하기
datalist = ( ("tom", "010-122-1234"), ("susie", "010-1234-1234"))
cur.executemany( "insert into PhoneBook values (?, ?);", datalist)

# 검색
cur.execute( "select * from PhoneBook;")
for row in cur:
    print(row)

# 마지막 정상 종료
con.commit()
con.close()
