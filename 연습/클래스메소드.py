class User:
    def __init__(self, name="", email="", phone=""):
        self.name=name
        self.email=email
        self.phone=phone

    # 매개변수들을 tuple 타입으로 전달받음
    # u1 = User.fromTuple(("홍길동", "hong@gmail.com", "010-0000-0000"))
    @classmethod
    def fromTuple(cls, tup):
        return cls(tup[0], tup[1], tup[2])
    
    @classmethod
    def fromDict(cls, data):
        return cls(data["name"], data["email"], data["phone"])
    
    def output(self):
        print(self.name, self.email, self.phone)
    

u1 = User("김길동", "kim@gmail.com", "010-1111-1111")
u2 = User.fromTuple(("홍길동", "hong@gmail.com", "010-0000-0000"))
u3 = User.fromDict({"name":"이길동", "email":"lee@gmail.com", "phone":"010-2222-2222"})

u1.output()
u2.output()
u3.output()