import random

class LottoData:
    def __init__(self, result=list() ):
        self.result = result

    def createLotto(self):
        while True:
            num = random.randint(1, 45)
            if num not in self.result:
                 self.result.append(num)
            if len(self.result)==6:
                break

    def display(self):
            print(self.result)

m1 = LottoData()
m1.createLotto()
m1.display()