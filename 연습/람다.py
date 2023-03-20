a = [1, 3, 4, 5, 6, 7, 86, 44, 32, 12, 14, 15, 21, 65]
colors=["red", "blud", "green", "yellow", "purple", "violet", "pink", "black"]
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


# 람다 : 파이썬의 경우 한줄짜리 임시 함수
# 파이썬의 경우 람다의 앞에 lambda를 입력하며 매개변수는 수식이 됨


# a로부터 짝수를 걸러내려고 할 때
# filter : 특정 조건을 만족하는 데이터리스트를 만들 때
# map : 배열의 모든 요소에 연산을 수행할 때
# zip : 여러개의 배열의 요소를 묶어서 tuple로 만들 때

# filter : 매개변수가 하나이고 반환값은 true/false인 함수를 전달하면 이 함수를 배열의 요소마다 호출하여 true인 데이터들만 반환

# 짝수를 추출하는 기존 함수 선언
def isEven(x):
    return x%2==0

b = filter(isEven, a)   # filter(함수, iterable 객체)
# 이 때, filter가 실행되지 않고 iterable 객체를 반환
# for문이나 list를 다시 사용해야 한다
print(b)

b = list(filter(isEven, a))
print(b)

for i in (filter(isEven, a)):
    print(b)

# 함수를 람다로 만들어 전달하기
# a 리스트의 요소들이 x로 전달됨
print("짝수추출")
for i in filter(lambda x: x%2==0, a):
    print(i)

# 단어 길이가 5글자 이상인 경우만 추출하기
print("5글자 이상")
for i in filter(lambda w : len(w)>=5, colors):
    print(i)

# 대문자
print("대문자로")
for i in map(lambda z : z.upper(), colors):
    print(i)

# key parameter : 정렬될 기준이 되는 키값(이 부분을 지워도 같은 결과가 출력됨)
# x를 기준으로 정렬하는 lambda 함수
wordsList = sorted(colors, key=lambda x : x)
print("정렬된 데이터")
print(wordsList)
print("원본 데이터")
print(colors)

# name을 기준으로 정렬
sortedDataList = sorted(dataList, key=lambda item:item["name"])
print("정렬된 데이터")
for item in sortedDataList:
    print(item)

print("원본 데이터")
for item in dataList:
    print(item)

# 원본을 정렬하려면 .sort함수를 바로 호출(reverse=True : 내림차순)
dataList.sort(key=lambda item:item["name"], reverse=True)
for item in dataList:
    print(item)

# zip : 여러개의 데이터를 한묶음으로 묶어줌
list1 = ["홍길동", "김길동", "이길동", "박길동"]
list2 = ["hong@gmail.com", "kim@gmail.com", "lee@gmail.com"]
list3 = ["010-0000-0000", "010-1111-1111", "010-2222-2222"]

for item in zip(list1, list2, list3):
    print(item) # 각각의 요소들을 tuple로 묶어서 전달

