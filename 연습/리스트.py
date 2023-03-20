words = ["apple", "pineapple", "orange", "banana", "lemon", "grape", "strawberry", "kiwi"]
print(words)    # java처럼 for문을 사용할 필요가 없다

# python의 리스트는 인덱싱과 슬라이싱이 함께 지원됨
print(words[0])
print(words[1])
print(words[2])

print(words[:3]) # 0, 1, 2
print(words[:3:2]) # 0, 2
print(words[::-1]) # 역순 출력
print(words[3:])    # 3, 4, 5...

words[0] = "potato"
print(words)

words[1:3] = ["red", "green"]   # 슬라이싱을 통한 값 변경
print(words)

# 데이터 추가
words.append("rainbow")
words.append("assembly")
print(words)

# 데이터 삭제
words.remove("red")
print(words)

# 확장 - 두 개의 리스트 병합
words.extend("blue")    # words.extend(['b', 'l', 'u', 'e'])로 인식함
print(words)

words.extend(["blue"])  # 리스트끼리의 병합을 원한다면 반드시 []괄호를 써줘야 한다
print(words)

# 인덱스 찾기
print(words.index("blue"))
# 찾아서 있다면 값 반환, 없다면 예외에러 발생
# print(words.index("magenta"))

# .count : 데이터 갯수를 세서 반환, 없다면 0 반환
print(words.count("magenta"))

if words.count("magenta")==0:
        print("magenta is not found")
else:
        print(words.index("magenta"))

if "magenta" not in words : # not in : list 안에 데이터가 없으면 true 반환
        print("magenta is not found")
else:
        print(words.index("magenta"))