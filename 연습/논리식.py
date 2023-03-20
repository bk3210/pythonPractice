a = int(input("a= "))

# and 연산은 단축평가, & 연산은 단축평가를 하지 않고 모든 연산에 대한 평가를 진행함
# True and True = True
# False and True = False
# False and False = False

# & : False 뒤에 오는 수식도 참/거짓연산을 한다
# True or 수식 : 뒤 수식은 참/거짓연산을 하지 않는다
# True | 수식 : 뒤 수식까지 참/거짓연산을 한다

if a & 10/a:     # a는 0보다 커야 하고 10/a의 결과도 0보다 커야 한다
    print(a)
else:
    print(a)