# demofile2.0

f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
print("---list로 받기---")
f.seek(0)
lst = f.readlines()
print(lst)
for item in lst:
    #print(item, end="")
    print( item.replace("\n", "") )

# 처음으로 파일커서 돌아가기
f.seek(0)
print( f.readline() )
print( f.readline() )


f.close()