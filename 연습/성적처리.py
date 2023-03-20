scoreList = []  # 전역객체

# 과목명을 가져오는 함수(ord로 과목명을 아스키 코드화하여 판단한다)
def isNumberic(s) : # 숫자로만 이루어진 문자열이면 True 반환
    for i in range(0, len(s)):
        if ord(s[i])<ord('0') or ord(s[i])>ord('9'):
            return False
        
    return True # True/False 마지막까지 왔다면 숫자로만 구성되어 있다는 뜻

def getNumber(subject):
    temp = input(subject+" : ")
    while not isNumberic(temp):
        print("정수만 입력하세요")
        temp = input(subject + " : ")
        # 정수일 때만 while문을 종료한다
    return int(temp)

def getScore(subject):
    temp = getNumber(subject)
    while temp<0 or temp>100:
        print("0~100사이의 점수만 입력하세요.")
        temp=getNumber(subject)
    return temp

def append():
    score = {}  # Java도 DTO를 만들지 않고 Map을 사용할 수 있다
                # Python의 dict타입은 HashMap과 유사
    score["name"] = input("이름 : ")
    score["kor"] = getScore("국어")
    score["mat"] = getScore("수학")
    score["eng"] = getScore("영어")
    score["total"] = score["kor"]+score["mat"]+score["eng"]
    score["avg"] = round((score["kor"]+score["mat"]+score["eng"])/3, 2)
    scoreList.append(score)

def output():
    for score in scoreList:
        print("{} {} {} {} {} {}".format(score["name"], score["kor"], score["mat"], score["eng"],
                                         score["total"], score["avg"]))
    
def start():
    while True:
        print("1. 입력")
        print("2. 출력")
        sel = input("선택 : ")
        if sel=="1":
            append()
        elif sel=="2":
            output()
        elif sel=="0":
            return
        
start()

# 총점, 평균 계산
# 데이터 입력시 에러 체크를 해야함
# (점수를 입력받아 숫자로 전환 가능한지 확인하고 숫자로 전환)
# (숫자가 아니면 에러발생, 0~100 사이여야 함)
# 100이 넘어가면 에러 체크하기