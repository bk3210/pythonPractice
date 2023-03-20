#Python에서는 Java의 for(int i=1; i<=10; i++){} 문법이 사라짐

# iterator 또는 Enumeration : 현재 모든 객체지향언어에 공통적으로 있는 개념
# 클래스를 만들 때 클래스가 컬렉션류일 때, 내부에 배열을 갖거나 linkedList 등의 무엇인가를 담아두어야 하는 클래스를 설계할 때
# 외부의 클래스 사용자가 클래스 내부의 실제 데이터 배치상태를 알 수 없어도 언제나 동일한 형태로 전체 데이터를 순회할 수 있도록
# 하는 인터페이스
# 데이터를 맨 처음 것부터 차례차례 다음 데이터로 이동하는 것을 보장
# iterator는 컬렉션 클래스를 만드는 쪽에서 제공

#for 변수명 in iterable 객체
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

#range(시작값,종료,증감치)  - iterable
print(list(range(1,11,1)))

# 한줄로 출력+마지막 줄바꿈
for i in range(1, 11):
    print(i, end=" ")
print()

# 2, 4, 6, 8, ... 짝수 출력
for i in range(2, 101, 2):
    print(i, end=" ")
print()

# 1, 3, 5, 7, ... 홀수 출력
for i in range(1, 101, 2):
    print(i, end=" ")
print()

# 100, 90, 80, ... 0의 앞 순서까지
for i in range(100, 0, -10):
    print(i, end=" ")
print()

# 1~100 한 줄에 10개씩 - for문 + if문
for i in range(1, 101, 1):
    print(i, end=" ")
    if i % 10==0:   # 10의 배수일 때 줄바꿈
        print()

# 1~100 한 줄에 10개씩 - 이중 for문
k=1
for i in range(0, 10):
    for j in range(0, 10):
        print(k, end=" ")
        k = k+1
    print()

# 문자의 아스키 코드값을 반환하는 함수
print(ord("A"))
print(ord("B"))

# 키보드로 문장을 입력받아서 문장안에 쓰인 문자의 갯수를 출력
# abstract class
# a ===> 3
# b ===> 1

