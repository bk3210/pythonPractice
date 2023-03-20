
# class 선언 : 파이썬은 객체를 만들지 않아도 클래스 멤버를 사용할 수 있음(메모리도 차지)
class Person:
    name="홍길동"   # 클래스 멤버
    age=23

    def output(self) : # 첫번째 매개변수로 self를 두고
                      # 객체 변수나 함수를 사용할 때 반드시 self를 붙임
        print("이름 : ", self.name)
        print("나이 : ", self.age)
        # self = java의 this

print(Person.name)
print(Person.age)
# 이 메모리는 기본적으로 public 속성임

p1 = Person()   # 인스턴스 생성
p1.output()