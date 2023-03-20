#x=list(input().split())
#for i in x:
#    if ord(x[i])==:
#    print(count())

# 문자의 아스키 코드값을 반환하는 함수
print(ord("A"))
print(ord("B"))

# 키보드로 문장을 입력받아서 문장안에 쓰인 문자의 갯수를 출력
# abstract class
# a ===> 3
# b ===> 1

s = input("문장 : ")
count = list()
for i in range(0, 26):      # 검색할 총 범위 : 알파벳 25개
    count.append(0)

for i in range(0, len(s)):
    if ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
        count[ord(s[i])-ord('A')]+=1
    elif ord(s[i])>=ord('a') and ord(s[i])<=ord('z'):
        count[ord(s[i])-ord('a')]+=1
    
for i in range(0, 26):
    print(chr(i+65), "===>", count[i])



s = input("입력하세요 : ")
list = []

for i in s:
    if i in list:
        s[i] +=1
    else:
        s[i] = 1
print(s)


