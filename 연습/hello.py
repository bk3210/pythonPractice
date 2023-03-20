# -*- coding: utf-8 -*-
# 에디터가 utf-8로 설정되어 있지 않아도 강제로 utf-8로 인코딩하는 문장
# 반드시 첫줄에 있어야 한다
print("hello python")

a=10 # a는 참조형(타입이 없음)
#a라는 변수에 저장된 값 10은 int형
print(a, type(a)) # 변수 a가 아니라 변수 a가 가리키는 값의 타입 출력

a = 4.5
print(a, type(a))

a='A'
print(a, type(a))

a="A"
print(a, type(a))
# python에는 문자타입(char)이 존재하지 않음
# '', "" 둘다 문자열(String)로 인식함

a = 3-4j #복소수
print(a, type(a))
