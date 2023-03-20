a = [1, 3, 4, 5, 6, 7, 86, 44, 32, 12, 14, 15, 21, 65]
b = a
# 얕은 복사와 깊은 복사
# 파이썬은 모든 변수가 참조형임(값이 아닌 참조값을 저장함)
# b = a를 하면 b 변수에는 a가 갖고있는 주소값이 복사되고, 둘은 같은 객체를 가리키게 됨

b[0] = 100
print("a=", a)  # b = a : 얕은 복사, 서로 같은 메모리
print("b=", b)

# 깊은 복사 : 새로운 메모리를 확보해 각자 다른 메모리를 기록할 수 있는 것
b = []  # 새로운 리스트 만들기
#b = list()로도 쓸 수 있다
for i in range(0, len(a)):
    b.append(a[i])

b[0] = -3
print("a=", a)
print("b=", b)
# 둘이 다른 메모리가 된다

# comprehension을 이용한 깊은복사 : [ 항목 for 항목 in 리스트]
c = [item for item in a]    # a 전체를 복사해 변수 c에 담는다(깊은 복사)
print("c=", c)

d = [item*2 for item in a]    # 배열의 값이 전체 x2한 값이 복사되어 들어감
print("d=", d)

# [항목 for 항목 in 리스트 if 조건식] : 조건식을 만족하는 리스트만 복사해서 전달하고, 나머지는 버림
# 항목의 변수명은 무엇이라 지어도 상관없지만 모두 일치해야 한다
c = [item for item in a  if item%2==0]

d = [item*2 for item in a]
print("d=", d)

print("짝수만 출력")
c = [item for item in a if item%2==0]
print("c=", c)

print("10보다 큰 수만 출력")
c = [item for item in a if item>10]
print("c=", c)


# 복사는 문자열의 배열값도 가능하다
colors=["red", "blud", "green", "yellow", "purple", "violet", "pink", "black"]

# 깊은 복사
c = [x for x in colors]
print("c=", c)

# 대문자로 바꾸어서 복사
c = [x.upper() for x in colors]
print("c=", c)

# 문자열 길이가 5글자 이상인 배열값만 대문자로 바꾸어서 복사
c = [x.upper() for x in colors if len(x)>=5]
print("c=", c)

# 문자열 안에 b 문자를 포함한 값만 복사
c = [x for x in colors if x.__contains__("b")]
print("c=", c)

# 단어에서 앞단어 3글자씩만 잘라서 복사 - 슬라이싱
c = [x[:3] for x in colors]
print("c=", c)

#list에 dict타입 깊은 복사
dataList = [
    {"name":"홍길동", "age":23, "phone":"010-0000-0000"},
    {"name":"김길동", "age":28, "phone":"010-1111-1111"},
    {"name":"이길동", "age":42, "phone":"010-2222-2222"},
    {"name":"박길동", "age":21, "phone":"010-3333-3333"},
    {"name":"최길동", "age":25, "phone":"010-4444-4444"},
    {"name":"정길동", "age":31, "phone":"010-5555-5555"},
    {"name":"강길동", "age":64, "phone":"010-6666-6666"},
    {"name":"조길동", "age":20, "phone":"010-7777-7777"},
    {"name":"윤길동", "age":47, "phone":"010-8888-8888"},
    {"name":"장길동", "age":66, "phone":"010-9999-9999"},
    {"name":"임길동", "age":18, "phone":"010-0001-0001"}
]

print(dataList)

dataList2 = [item for item in dataList]
for item in dataList2:
    print(item)

# 나이가 30이상인 사람들 추출
print("나이 30 이상")
dataList2 = [item for item in dataList if item["age"]>=30]
for item in dataList2:
    print(item)

# 전화번호에 9가 들어가는 사람들 추출
print("전화번호에 9 들어가는 사람")
dataList2 = [item for item in dataList if item["phone"].__contains__("9")]
for item in dataList2:
    print(item)
    
# 성이 장 또는 홍씨인 사람들 추출
print("장씨나 홍씨")
dataList2 = [item for item in dataList if item["name"].startswith("장") or item["name"].startswith("홍")]
for item in dataList2:
    print(item)