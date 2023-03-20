import pandas as pd

# dict 타입 안에 list 구조
data = {
    "name":["홍길동", "김길동", "이길동", "박길동"],
    "kor":[90, 90, 90, 90],
    "eng":[80, 80, 80, 80],
    "mat":[70, 70, 70, 70]
}

df = pd.DataFrame(data)
print(df)
print()

# iloc = indexing을 통해 접근
print(df.iloc[0],[0])
print()

# 필드명으로
print(df.loc[0, "name"])
print()

# 0번째 행
print(df.iloc[0, :])
print()

# 행의 이름이 0, 1, 2, 3
print(df.loc[0, :]) # :를 써주면 한 행이 출력됨
print()

# 열
print(df.iloc[:, 1])
print(df.loc[:, 'name'])
print()

# 홍길동, 이길동 데이터만 추출
# 특정행or열만 추출하고 싶다면 행or열의 인덱스를 리스트로 만들어 전달
print(df.iloc[[0, 2], :])
print()

# 열 추출하기('name', 'eng', 'mat')
print(df.loc[:, ['name', 'eng', 'mat']])
print()

# 다른 객체로 복사하기
df2 = df.loc[0:4, ['name', 'mat', 'eng']]
print(df2)
print()

# 데이터 추가 : dict 타입을 이용해 추가
#   list 타입은 추가시 원본 객체가 바뀜
#   dataframe타입은 항목이 추가된 새 객체를 반환 - 반환값을 저장해야 추가 완료됨
print("------------")
df = df.append({"name":"최길동", "kor":99, "mat":88, "eng":77},
               ignore_index = True)
# ignore_index : 반드시 True
# 데이터 추가시 인덱스를 새로 부여해야 하는데 기존 인덱스를 무시하겠느냐는 뜻
print(df)
print()

# df = df.append({"name":"정길동", "kor":99, "mat":88, "eng":77},
#                ignore_index = True)
# df = df.append({"name":"강길동", "kor":88, "mat":77, "eng":88},
#                ignore_index = True)
# df = df.append({"name":"조길동", "kor":77, "mat":99, "eng":99},
#                ignore_index = True)

# 최근 버전에서는 .append 대신 concat 사용 권장
# concat : 원래 기본적으로 병합(열 또는 행)을 수행
# concat([df1, df2, df3], 병합조건)
# axis = 0 : 축이 이 행임을 의미
df = pd.concat([df, pd.DataFrame({"name":["윤길동"], "kor":[98], 
                                  "eng":[88], "mat": [78]})], axis = 0, ignore_index=True)

# 컬럼명 확인
print(df.columns)
print()

# 새로운 컬럼명 부여
df.columns = ["이름", "국어", "수학", "영어"]
print(df)
print()

# 새로운 컬럼 추가
df["합계"]=df["국어"] + df["수학"] + df["영어"]
df["평균"]=df["합계"]/3
print(df)
