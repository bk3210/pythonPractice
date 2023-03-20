# 함수는 어디에서든지 선언 가능하다 : 전역함수
def add(x, y):
    return x+y

print(add(5, 4))
x = 10
y = 20
print(add(x, y))

# 함수 주소를 다른 변수에 저장 가능(파이썬에서는 함수를 변수로 간주함) - c언어의 관점
calc = add      # add 함수가 가지고 있는 인덱스값을 calc 변수에 저장 가능
print(calc(1, 12))     # Java는 이 기능을 인터페이스로 대신 처리한다

# 1~limit까지의 합계를 구하여 반환하는 함수
def sigma(limit):
    if limit< 1:    # 함수를 sigma(0)으로 호출하면 0이 limit보다 작아서 none을 반환하고 종료됨
        return  # 값을 보내지 않을 경우에 None이 반환됨
    
    s = 0
    for i in range(1, limit+1):
        s += i

    return s

print(sigma(0))
print(sigma(10))
print(sigma(100))

def isZero(args1):
    return args1==0 #   == : 연산 수행 결과를 반환(0이 맞는지 아닌지)

print(isZero(6))
print(isZero(0))


def changeValue(a):
    a = a*10
    return a

x = 11  # 지역변수 x와 매개변수 a가 생성되는 영역은 서로 다르다
# 함수가 호출될 때 x에 저장된 값이 a로 복사된다
# a 값을 바꾸어도 x와 a는 서로 다른 메모리공간을 차지하기 때문에 서로 영향을 미치지 않는다

# 즉, 값을 바꾸기 위해서는 함수의 return값을 받아와야 대입할 수 있다
x = changeValue(x)
print("x = ", x)

# 단, list 타입은 함수 return을 하지 않아도 매개변수에 값을 담아 전달하는 게 가능하다
# 값이 아니라 주소가 전달되기 때문에 직접 접근이 가능
a = [0, 0, 0, 0, 0]
def setValue(aa) : 
    for i in range(0, len(a)):
        aa[i] = i+1

setValue(a) # list 타입이 전달되면 값을 바꿔서 온다
print(a)

def setDictValue(colors):
    colors["red"]="빨강"
    colors["green"]="초록"
    colors["purple"]="보라"
    colors["yellow"]="노랑"

out_colors={}   # dict 객체를 생성할 때 : {} 또는 dict()
setDictValue(out_colors)
print(out_colors)

a = [3, 6, 4, 1, 11, 17, 15, 77, 34, 10]

# 옛날 방식으로 짝수, 홀수 구분하는 소스
oddList = []
evenList = []
for i in a:
    if i%2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
print(oddList)
print(evenList)

# comprehension : 축약, 압축
print([i for i in a if i%2==0]) # 짝수 추출
print([i for i in a if i%2==1]) # 홀수 추출