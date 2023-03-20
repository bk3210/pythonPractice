# tuple : 리스트와 유사, 리스트는 데이터 읽고쓰기 둘 다 가능/튜플은 readonly
# 처리 속도가 빠름
# 데이터를 한 덩어리로 묶어주는 역할을 함

a, b = 5, 6
print("a = ", a)
print("b = ", b)

a = (1, 2, 3, 4, 5)
print(a, type(a))

# 인덱싱, 슬라이싱이 적용되나 값 수정은 불가능
# a[0] = 10         에러 발생

for i in a:
    print(i)

print(a[0:3])
print(a[::-1])

# 메소드 만들기
def add(x, y):
    # add(x, y)의 매개변수들은 외부의 값을 읽어온 다음 외부 지역변수 x, y와의 연관성이 사라짐
    # 즉, 함수 내부에 영향을 미치지 않음
    x = x*2
    y = y*2
    return x, y # 원래 함수는 값을 하나만 반환할 수 있음
    # 하나만 반환해야 하므로 두 값을 묶어 하나의 튜플 객체로 만듦
    # 튜플은 자바에 없음

# 위 add(x, y)의 매개변수와 이 x, y는 서로 연관이 없다
x=1
y=7

print(type(add(x, y)))
x, y = add(x, y)    # 메소드 수행후 결과를 tuple로 반환
# 별도의 변수에 tuple값을 하나씩 할당함
print("x = ", x)
print("y = ", y)