# 파일명을 영어로 쓰면 실제 Numpy파일과 충돌이 생길 수 있음
# cmd 관리자권한 실행 -> pip install numpy 입력 : pip 명령어가 인터넷을 검색해서 해당 파일 설치를 실행
import numpy as np
# numpy는 c타입

a = [1, 2, 3]   # list 타입
a1 = np.array(a)    # list -> numpy 타입으로 전환
print(a)
print(a1)