import pandas as pd
import numpy as np
s = pd.Series([1, 2, 3, np.nan, 5, 6, 7, np.nan])
print(s)
print(s.isnull())   # 각 요소가 NaN이면 True, 아니면 False 반환
print()

# 하지만 데이터 건수가 많아지면 이런 방식으로 누락치를 걸러낼 수는 없다
print(s.isnull().sum()) # 결과가 True인 것(누락 데이터)의 건수를 센다
print()

# 데이터프레임 : 각 필드별로 하나의 필드라도 NaN이 있다면 그 행을 완전히 삭제
#   이 방식은 지나치게 많은 삭제량이 발생할 수 있음
#   또는 대체를 하기도 한다(평균값 or 중간값(비범주형 자료), 최빈수(범주형) 등으로)

data = pd.read_csv("./data2/data.csv")
print(data.info())  # 이걸 통해서도 데이터 갯수에 누락치가 있는지 확인 가능
print(data.head())
print(data.columns)
# print(data["weight"].mean())
print()

# 필드에 NaN값 확인방법
# dropna=False는 NaN값도 같이 카운트해준다 - 카테고리 타입에 적합
print(data['height'].value_counts(dropna=True))
print()

print(data['height'].isnull())  # NaN일 때 True 반환- 주로 이걸 많이 씀
print()
print(data['height'].notnull()) # NaN일 때 False 반환

#NaN값을 카운트
print(data['height'].isnull().sum())
print(data['weight'].isnull().sum())
print()

# 처리방법 1. 삭제
# axis=1은 삭제의 방향을 지정하는 속성, 열 삭제(NaN값을 포함한 열이 있을 때 그 열을 삭제시키라는 뜻)
# thresh : 삭제를 하되 NaN이 아닌 데이터가 28건 이상 들어있는 열은 제외(삭제 배제조건)
# 여기서 발생하는 삭제는 원본 삭제가 아님(자주 쓰지 않음)
data2 = data.dropna(axis=1, thresh=28)
print(data2)
print()

# thresh 없이 NaN값은 무조건 삭제
data3 = data.dropna(axis=0, thresh=2)
print(data3.shape)
print(data3['weight'].isnull().sum())
print(data3['height'].isnull().sum())
print()

#subset ; 필드를 묶어서 처리
# height에 NaN값이 들어있으면 삭제
data2 = data.dropna(subset=['height'], how='any', axis=0)
print(data2.shape)

# height, weight 둘중 NaN값이 있으면 삭제
data2 = data.dropna(subset=['weight', 'height'], how='any', axis=0)
print(data2.shape)

