import pandas as pd

df = pd.read_csv("./data/auto-mpg.csv")
# 이 방식은 실제 데이터가 많을 경우 식별이 불가능해진다
#       전체 구조를 확인하기 위한 함수들이 따로 있음
print(df.head())    # 앞쪽에서부터 데이터 5건만 출력
print()

print(df.head(10))  # 10줄 출력
print()

print(df.tail())    # 뒤쪽에서 5줄
print(df.tail(10))
print()

# 각 필드들에 대한 간략한 설명(데이터 건수, 타입 등등)
print(df.info())
print()

# describe : 기초 통계값
print(df.describe())
print()

print(df.columns)
# 실린더 갯수가 4개인 조건을 줬을 경우
# 실린더 갯수가 4인 데이터에 대해 True, 아니면 False를 데이터 갯수만큼 반환
print(df.cylinders==4)

print(df[df.cylinders == 4])    # 실린더 갯수가 4인 데이터 추출

df3 = df[df.cylinders == 4]     # 실린더 갯수가 4인 데이터를 따로 추출해서 저장
print(df3.shape)

# 평균 연비 이상의 데이터 추출
# 먼저 평균 연비를 구함
mpg_mean = df["mpg"].mean()
print("연비 평균 : ", mpg_mean)

df3 = df[df.mpg >= mpg_mean]
print(df3.head())

# 연비, 마력 둘 다 평균이상
#   and연산은 pandas의 것이 아닌 파이썬의 함수이기 때문에 벡터 연산을 실행하지 않는다
#   numpy 라이브러리 import
import numpy as np

hp_mean = df["horsepower"].mean()
df3 = df[np.logical_and(df.mpg >= mpg_mean, df.horsepower>=hp_mean)]
print(df3)

print(">>>>>>>iris 예제<<<<<<<<")
df2 = pd.read_csv("./data/iris.csv")
print(df2.info())
print()

print(df2.head(7))
print()

print(df2.describe())
print()

print(df2.shape)    # 행과 열의 갯수
print()

# 4) variety 이 Setosa 인 데이터의 통계량을 출력하세요
df3 = df2[df2['variety']=='Setosa']
print(df3.head())
print()

# 데이터 : 범주형/비범주형
# 범주형 자료타입 : 연속적이지 않음. 종류, 선호도(1.5를 선택하지 않음)
# 범주형, 카테고리타입, 팩터타입 : 평균이 중요하지 않고 발생 빈도수를 중시
# value_counts : 발생 빈도수 구하는 함수
# 비범주형은 연속된 값, 평균이 중요(집값, 몸무게, 키)
# 빈도수 테이블 : 데이터가 

# 5) 각각 variety가 Setosa, Virginica Versicolor 의 sepal.length 값의 평균값을 출력하시오
setosa_avg = df2[df2['variety']=='Setosa']
print(setosa_avg["sepal.length"].mean())



# 필드명 안에 .이 있으면 충돌날 수 있음 + 새로운 필드 추가할 때는 .필드명을 사용할 수 없음
#   ir1["sepal.length"] 이런 식으로 써줘야 함
setosa_avg = df2[df2.variety=='Setosa']
print(setosa_avg["sepal.length"].mean())

vv_avg = df2[df2.variety=='Virginica Versicolor']
print(vv_avg["sepal.length"].mean())
print()

