import math
# 자바의 import : 이미 메모리에 내장된 라이브러리를 단축이름을 통해 실제이름으로 찾아가는 것
# 파이썬의 import : 라이브러리를 메모리로 가져오라는 뜻

print(math.gcd(4, 24))  # 최대공약수
print(dir(math))    # 라이브러리 내 메소드 알려줌

print(math.ceil(4.3))   # 올림
print(math.ceil(4.9))

import os
print(os.curdir)   # 현재 디렉토리
print(os.getcwd())  # 현재 경로