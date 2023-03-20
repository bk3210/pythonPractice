# dict 타입: dictionary의 약자. 자바의 HashMap과 유사
# 인덱싱/슬라이싱 불가, 키+값의 쌍 형태로 값을 저장함
# JSON과 유사한 형태
mydic = {"red":"빨강", "green":"초록", "blue":"파랑"}
print(mydic["red"])
# print(mydic.green) 은 에러남

# 추가
mydic["black"]="검정"
print(mydic["black"])

# 수정
mydic["red"]="빨간색"
print(mydic["red"])

# 삭제
del mydic["red"]
print(mydic)