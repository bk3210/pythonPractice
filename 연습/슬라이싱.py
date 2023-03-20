s = "Hello Python"  # s는 문자열이지 배열이 아닌데도 배열처럼 인덱싱이 가능함
print(s[0]) # 인덱싱 : 자바 - s.charAt(0)
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 슬라이싱 : [시작:종료:증감치]
print(s[::])    # 전체 출력
print(s[0:5])   # Hello
print(s[0:8:2]) # 0, 2, 4, 6번째 자리 문자 출력(마지막 8은 제외)
print(s[::-1])  # 뒤에서부터 역순으로 출력
# 시작:종료:증감치에서 시작과 종료는 음수를 사용할 수 없음(버전에 따라 다름)
print(s[7:0:-1])

# s[0] = 'h'  # 문자열은 인덱싱으로 값 바꾸기가 불가능함
s = "h" + s[1:] # 특정 문자열을 바꾸고자 할 때
print(s)

# 문자열 바꾸기 : .replace
s = "I like star. red star. blue star"
s = s.replace("star", "moon")   # 리턴값을 넣어줘야 한다
print(s)