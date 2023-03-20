s = "hello"

#iterator : 사용자가 내부 데이터 구조를 알지 못해도 항상 같은 방법으로 내부 데이터에 접근하게 함

it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


a = [1, 2, 3, 4, 5]
ait = iter(a)
print(next(ait))
print(next(ait))
print(next(ait))
print(next(ait))
print(next(ait))


# tuple, list, dict 전부 iterator 가능

def generator(): # 무한 숫자 생성
    i=1
    while True:
        # return i    # 함수 종료
        yield i     # 함수 호출시 여기까지의 동작 결과를 저장, 값을 보냄(return과 다름)
        i = i+1     # return을 하면 이 줄은 실행불가

# 원래 함수는 작업이 끝나면 메모리 정리 작업에 의해 매개변수 i가 삭제됨
# 그러나 yield 메소드를 실행시키면 함수가 값을 보낸 뒤에도 정리되지 않고 메모리를 차지하게 됨 - 무한동작
#for i in generator():
#    print(i)

def generator2(limit=10):
    i=1
    while i<=limit:
        yield i
        i = i+1

print("두번째 제너레이터")
for i in generator2():
    print(i)

