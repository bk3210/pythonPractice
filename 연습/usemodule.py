import mymodule

print("모듈 사용")

print(mymodule.sigma(100))
print(mymodule.circle(7))
print(mymodule.toUpper("korea"))

# import 구문은 모듈명.메소드명() 형태로 사용해야 함
from mymodule import sigma, circle, toUpper
# 이거 쓰면 모듈명 생략하고 이 파일 메소드인 것처럼 사용 가능

print(sigma(50))
print(circle(9))
print(toUpper("hello new year, happy new year"))