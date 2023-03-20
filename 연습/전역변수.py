g_x = 10

def myfunction():
    global g_x  # 전역변수를 사용하겠다는 뜻(없으면 에러 발생)
    g_x = g_x + 1
    print(g_x)

myfunction()

# g_x는 함수 바깥에 존재하는 전역변수
# 단, 파이썬에서는 전역변수를 자주 쓰지 않는 것이 바람직함