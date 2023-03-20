# 나이를 입력받아 성인여부 판단하기
age = int(input("나이를 입력하세요 "))  # 이 때 input으로 받는 값은 str -> int형변환 필요
if age>=19:
    print("성인입니다.")
else:
    print("미성년자입니다.")


score=int(input("성적을 입력하세요 "))
if score>=90:
    print("수")
elif score>=80:
    print("우")
elif score>=70:
    print("미")
elif score>=60:
    print("양")
else:
    print("가")