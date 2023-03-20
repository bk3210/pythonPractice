class Person:
    # 클래스 내부에 선언된 변수는 클래스의 소속, 객체가 아님
    # 객체를 새로 생성할 때 메모리가 할당되지 않음(자바는 객체 생성시 메모리 할당)
    # static을 쓰지 않아도 static처럼 인식됨(객체와 상관없음)
    name="홍길동"   # 변수만 선언하는 방법이 없음, 값을 할당해야 함
    score=list()    # list 객체 생성
    
    # 버전 따라서 다르게 동작 가능, 변수를 생성자에서 선언해야 함
    # 생성자 : __init__
    def __init__(self, name="", score=list()):
        self.name=name
        self.score=score
        # 파이썬의 생성자는 한개만 만들 수 있다
        # 생성자를 만들면 매개변수값을 반드시 줘야 함
        # 생성자를 선언하면 기본 생성자가 자동으로 생성되지 않음 - 에러 발생


    def append(self, name="", score=[100, 90, 80]):
        self.name = name
        self.score = score
    
    def output(self):
        print(self.name, self.score)


p1 = Person()   # Person클래스 객체 생성
p1.append("홍길동", [90, 90, 90])

p2 = Person()
p2.append("김길동", [80, 80, 80])

p1.score[0]=1000
p1.output()
p2.output()

# 클래스에 새로운 변수를 추가할 수 있다(자주 쓰진 않음)
Person.phone="010-0000-0000"
print(p1.name, p1.score, p1.phone)

# 객체에도 사용 도중에 새로운 변수 선언이 가능
p2.address="서울시"
print(p2.name, p2.score, p2.phone, p2.address)


# 클래스 상속
class Student(Person):
    def __init__(self, name="", score=list(), className=""):
        Person.__init__(self, name, score)  # 부모 클래스 생성자 호출
        self.className=className

    def output(self):
        print(self.name, self.score, self.className)

s1 = Student("학생1", [100, 100, 100], "3-1")

# 파이썬의 클래스도 최상위 클래스로 object를 상속받음
print(isinstance(s1, Student))
print(isinstance(s1, Person))
print(isinstance(s1, object))   # 셋다 True


# static method
class TestClass:
    # 변수명 앞에 __붙이면 private
    __insCount=0

    # TestClass 객체가 몇개 만들어졌는지 확인
    def __init__(self):
        TestClass.__insCount+=1
        # self가 아니고 클래스 멤버이므로 클래스를 이용해 접근
        # 객체가 생성될 때마다 __insCount 변수값이 증가

    # __insCount값을 출력하는 함수
    def staticPrintCount():     # static 메소드
        # 매개변수에 self를 쓸 수 없다
        # 객체에 속한 메소드가 아니므로 객체를 뜻하는 self를 쓰지 않음
        print("카운트 : {}".format(TestClass.__insCount))

    # static메소드로 만들어주는 작업이 필요
    SPrintCount = staticmethod(staticPrintCount)

    # 자바의 어노테이션 - 파이썬의 데코레이터
    # static 메소드로 전환하는 최신 문법
    @staticmethod
    def staticPrintCount2():
        print("카운트 : {}".format(TestClass.__insCount))

    # 클래스 메소드 : 매개변수로 클래스 전달
    @classmethod
    def classPrintCount(cls):
        print("카운트 : {}".format(cls.__insCount))


t1 = TestClass()
TestClass.staticPrintCount()
TestClass.SPrintCount()

t2 = TestClass()
TestClass.staticPrintCount() # 이거나
TestClass.SPrintCount() # 이거 둘 중 아무거나로 호출가능



# t1 = TestClass()
# print(t1.__insCount)    # private라 접근x

