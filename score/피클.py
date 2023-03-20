# 피클 라이브러리 : 객체를 저장해 읽고쓰기(직렬화)를 할 수 있다
#   객체를 바이트 배열로 바꿔야 함
# 파이썬은 이 기능을 피클 하나로 구현

import pickle

# 파일에 객체 저장
colors = {"red":"빨강", "green":"초록", "blue":"파랑"}
file = open("test.bin", "wb")   # w-write, b-binary 이진파일 생성
pickle.dump(colors, file=file)
file.close()

# 파일에서 객체 읽기
colors = {}
file = open("test.bin", "rb")   # r-read
colors = pickle.load(file=file)
file.close()

print(colors)