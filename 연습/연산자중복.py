# 연산자 중복 : 이미 존재하는 연산자에 새로운 기능을 부여할 때 사용
# ex. + 본래기능은 더하기연산 / 문자열 연결도 가능한 것처럼
# 자바에는 없음, C, C++, Python에 있음

# 행렬 클래스
class Matrix:
    def __init__(self, mat1=None):
        if mat1==None:
            self.mat1 = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                         ]
        else:
            self.mat1=mat1
    
    def output(self):
        for i in range(0, len(self.mat1)):
            for j in range(0, len(self.mat1[i])):
                print("{0} ".format(self.mat1[i][j]), end=" ")
            print()

    # 2차원 형태의 배열끼리 더하는 메소드
    # __ : 연산자 오버로딩
    # m3 = m1 + m2를 할 경우 __add__를 호출함
    def __add__(self, other):
        temp = list(list()) # 2차원 형태 배열
        for i in range(0, len(self.mat1)):
            item=list()
            for j in range(0, len(self.mat1[i])):
                item.append(self.mat1[i][j] + other.mat1[i][j])
            temp.append(item)
        return Matrix(temp) # 객체를 만들어 반환 


m1 = Matrix()   # 데이터 없을 때
m2 = Matrix([[2, 3, 4], [2, 3, 4], [3, 4, 5]])    # 데이터 있을 때
m1.output()
m2.output()
# m3 = m1.add(m2)
m3 = m1 + m2    # 연산자 오버로딩을 할 경우 위 주석처럼 쓰면 에러발생
m3.output()