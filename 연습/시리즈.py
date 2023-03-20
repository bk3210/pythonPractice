import pandas as pd

data = [10, 20, 30, 40, 50] # list타입
# pandas의 series 타입으로 전환
series = pd.Series(data)
print(data)
print(series)   # 인덱스가 있어도 특별히 지정하지 않으면 0, 1, 2, 3, 4
print()

print([a for a in data if a>30])    # 파이썬 식
print()

# numpy도 가능
# print(data>30)  # 에러 발생 : 스칼라(변수 한개) 단위로 연산을 수행해서

# 수학 라이브러리들은 벡터(1차원, 2차원 등의 배열 형식) 단위로 연산을 수행한다
print(series>30)    # 결과를 실행해서 조건에 따라 True, False 반환
print(series[series>30])    # series에서 원하는 정보만 추출
print()

# 스칼라 연산
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
c = a + b
print(c)    # 1, 2, 3, 4, 5, 2, 4, 6, 8, 10
print()

sa = pd.Series(a)
sb = pd.Series(b)
sc = sa + sb    # 벡터연산 : 1차원 배열의 배열값끼리 연산 수행
print(sc)
print()

# 인덱싱, 슬라이싱도 가능
print(sc[0])
print(sc[2])
print(sc[0:3])
print()

# 단, 파이썬과는 차이가 있다
print(sc[[2, 4, 3]])  # 2, 4, 3번 데이터 추출(집합이라서 괄호 한번 더 치기)
print()

# 조건식을 직접 물어보면 벡터 전체에 대한 결과를 반환한다
print(sc>10)    # true/false값 반환
print()

print(sc[[True, True, False, False, False]])  # 맞는 결과만 추출(모든 인덱스값을 다 부여해야함)
print(sc[sc>10])    # 위와는 다른 결과가 나옴
print()

# dict타입을 시리즈로 만들면 앞의 키값들이 인덱스가 된다
data={"one":1, "two":2, "three":3, "four":4, "five":5}
s1 = pd.Series(data)
print(s1)
print(s1["one":"three"])
print(s1[0:3])
print()

print(s1[["two", "three", "four"]])
print(s1[[2, 0, 1]])
print()

# 특정 집단에 대한 보편적 성격 : 평균, 최대빈도, 최소빈도 등의 다양한 기준 있음
# 평균은 왜곡될 가능성이 있음
# 분산 : 오차와 기대치의 차이
#   분산이 크다 : 최소값과 최대값 사이의 차이가 크다
# 분산 : 오차의 제곱의 합(제곱을 하면 오차가 커지므로 편차가 더 눈에 잘 보임)
# 평균 : 70     60, 80, 50, 90, 70
#   수학적으로 음수를 제거하고 싶으면 절대값을 구하거나 제곱을 구함
#   총 오차의 합은 언제나 0
# 편차 : 분산의 제곱근(분산에 루트)

# series에는 기초 통계학에 관련된 대부분의 함수가 내장되어 있다
print("합계 : ", s1.sum())
print("평균 : ", s1.mean())
print("표준편차 : ", s1.std())
print("최대값 : ", s1.max())
print("최소값 : ", s1.min())
print("중간값 : ", s1.median())