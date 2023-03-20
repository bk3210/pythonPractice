# python은 생성자를 통해 변수를 선언한다
class ScoreData:
    def __init__(self, name="", kor=0, mat=0, eng=0):
        self.name=name
        self.kor=kor
        self.mat=mat
        self.eng=eng
        self.process()

    # 총점, 평균 구하기
    def process(self):
        self.total = self.kor + self.eng + self.mat
        self.avg = self.total/3
        if self.avg>=90:
            self.grade="수"
        elif self.avg>=80:
            self.grade="우"
        elif self.avg>=70:
            self.grade="미"
        elif self.avg>=60:
            self.grade="양"
        elif self.avg>=50:
            self.grade="가"

    def display(self):
        print("{} {} {} {} {:.2f} {}".format(self.name, self.kor, self.mat, self.eng, self.total, self.avg, self.grade))

