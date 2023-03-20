# 구구단 - 예전문법
# "형식" %(tuple타입)
for i in range(1, 10):
    print("%s x %d = %d" % (4, i, 3*1))

# 서식 : format 함수
for i in range(1, 10):
    print("{} {} {}".format(4, i, 3*i))

# 서식 : f-string함수
for i in range(1, 10):
    print(f"{i} X {3} = {3*i}")

# 10, 20, 30, 10, 30
print("{0} {1} {2} {0} {2}".format(10, 20, 30))

# 자릿수 10칸을 차지하고 앞에 공백 추가 - 오른쪽 정렬
print("{:>10}**".format(5))
# 앞에서부터 숫자를 출력하고 10칸을 확보    - 왼쪽 정렬
print("{:<10}**".format(5))
# 중앙 정렬
print("{:^10}**".format(5))
# 소수점 이하 2자릿수만 출력
print("{:.3}**".format(10/3))
# 3자리수마다 쉼표
print("{:,}**".format(10000000000000000000))


"""
ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
C...
D...
...
ZABCDEFGHIJKLMNOPQRSTUVWXY
"""

#a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#for i in a:
#    print(i)
#    if i

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, 26):
    print(s)
    s = s[1:]+s[0]

# 이중 for문
for i in range(3, 6):
    print()
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

# break / continue
for i in range(1, 11):
    print(i)
    if i==5:
        break   # i값이 5일 때 for문 종료

for i in range(1, 11):
    if i==5:
        continue    # 특정 조건을 만족시키면 다음 문장들을 수행하지 않고(건너뜀) 루프로 돌아감
    print(i)


# flag라는 변수를 삽입해서 for문을 거치고 나온 결과가 맞는지 확인
flag = False
for i in range(1, 11):
    print(i)
    if i==5:
        flag=True
        break

if flag:
    print("break문을 거쳤음")
else:
    print("그냥 종료")

for i in range(1, 11):
    print(i)
    if i==5:
        break
else:
    print("break문 수행이 없을 때")

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(a[0][0])
print(a[0][1])
print(a[0][2])

print(a[1][0])
print(a[1][1])
print(a[1][2])

