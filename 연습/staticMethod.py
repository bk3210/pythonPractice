class MyType:
    @staticmethod
    def isCapital(s):
        for c in s:
            if(ord(c)<ord('A') or ord(c)>ord('Z')):
                return False
        return True # for문을 수행해도 return되지 않았다면 전부 대문자이므로 True 반환
    
    @staticmethod
    def isNumeric(s):
        for c in s:
            if(ord(c)<ord('0') or ord(c)>ord('9')):
                return False
            return True
        
# static method는 객체를 생성하지 않고도 사용 가능
# 공유할 데이터가 없는데 기능적 유사성이 있을 때
# Java의 Math 클래스처럼 수학 연산 처리에 주로 사용됨
print(MyType.isCapital("TEST"))
print(MyType.isCapital("Test"))
print(MyType.isCapital("test"))

print(MyType.isNumeric("123"))
print(MyType.isCapital("T123"))