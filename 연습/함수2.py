# 기본값
# 파이썬에서는 오버로딩을 할 수 없음
# 그대신 매개변수에 기본값을 부여하여 오버로딩과 같은 효과를 냄(자바스크립트와 유사)
def myadd(a=10, b=20, c=30):
    return a+b+c

print(myadd())  # 60
print(myadd(1)) # a=1, b=20, c=30
print(myadd(1, 2))  # a=1, b=2, c=30
print(myadd(1,2,3)) # a=1, b=2, c=3

print(myadd(b=100, a=32)) # 순서 상관없이 매개변수 지정 가능

# sep = 공백 지정
print(1, 2, 3, sep="*", end=" ")
print(4, 5, 6, 7, sep="*")

# 함수의 파라미터를 dict타입으로 받고싶을 때는 변수 앞에 **를 붙임
def myfunc(**info):
    for key in info.keys():
        print(key, info[key])

myfunc(url="www.google.com", port=9090, param="x")

# 재귀함수(recursive) : 자기 자신을 호출하는 함수. 트리순회, in/post/preorder 순회할 때
# 수식전환시 유용
# 단점 - 느리고 메모리를 많이 차지함. 스택 오버플로우의 위험가능성
# 퀵 정렬 - 자바로 구현시 시스템자원을 전체 사용할 수 없으므로 오류가 발생할 수 있음

# 1+2+3+4.....+10
"""
f(n) = n + f(n-1)
f(10) = 10 + f(9)
f(9) = 9+f(8)

"""
def sigma(n=10):
    if n==1:
        return 1
    else:
        print(n)
    return n+sigma(n-1)

print(sigma())  # 10까지 더하기
# print(sigma(100))   # 100까지 더하기

# pass : 그 자체로는 아무 동작도 하지 않음, 미작성된 메소드의 블록 역할을 함
# class, method, if, for, while 아무데나 다 사용 가능
def myfunction():
    pass

# __doc__ : 속성값, 함수의 설명 출력
# __로 시작하는 변수나 함수는 특수목적, 보통 private 접근권한을 가짐
print(print.__doc__)
