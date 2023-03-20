a = 10
b = 3

print(a, '+', b, '=', a+b)
print(f"{a} - {b} = {a-b}")   # fstring : 문자열 가공 기능(문자열 앞에 f를 붙이고, "{변수명} or {수식}"을 지정하면 결과값이 출력됨)

print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")     # 정수 / 정수의 결과가 실수
print(f"{a} // {b} = {a//b}")   # 정수// 정수의 결과가 정수
print(f"{a} % {b} = {a%b}")     # 나머지 연산