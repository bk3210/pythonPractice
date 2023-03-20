def sigma(limit=10):
    s=0
    # range가 마지막 순서까지 연산을 하지 않기 때문에 limit+1
    for i in range(1, limit+1):
        s = s+i

    return s

def circle(radius=5):
    return radius*radius*3.14

# chr(코드) -> 문자
# ord(문자) -> 코드
def toUpper(s):
    temp=""
    for c in s: # 소문자일 때만 대문자로 바꿈
        if(ord(c)>=ord('a') and ord(c)<=ord('z')):
            temp = temp+chr(ord(c)-32)
            # a : 65, A : 97(97-65=32만큼 빼줘야 대문자로 바뀜)
        else:   # 나머지는 그냥 더함
            temp = temp+c
    return temp
    
# 내가 main으로 사용할수도 있고, 다른 모듈에서 import되어 사용할 수도 있음
print(__name__) # 내장변수, main으로 사용될 때는 __main__이라는 이름이, 모듈로 사용될때는 파일명으로 온다

if __name__ == "__main__":
    print(sigma(100))
    print(circle(5))
    print(toUpper("I like star"))
