# 파일처리
# 1. 텍스트 파일
#    txt, .ini, 소스파일(.java, .py) 등
#    컴퓨터 메모리에서 외부장치로 저장될 때 엔터키를 \r\n, \n 등의 형태로 가공해서 저장(OS에 따라 다름)
# 2. 이진파일
#    이미지, 동영상 등의 실행파일
#    저장시 컴퓨터 메모리에서의 형태 그대로 저장한다
# 텍스트 파일과 이진 파일은 읽고 쓰는 방식이 서로 다르다
"""
파일 읽고 쓰기 절차

파일 열기   open 함수
읽고 쓰기   
파일 닫기   close 함수
"""



# 1. 텍스트 파일 읽기모드로 열기 : open("파일명", "모드", 인코딩 형식)
f = open("test.txt", "r", encoding="utf-8")
# 한글의 경우 반드시 인코딩을 해야한다
# r은 읽을 파일의 참조를 가지고 있다
lines = f.readlines()   # 텍스트 파일을 한꺼번에 다 읽어온다
for line in lines:
    # korea\n   [0:len('korea')-1]
    line = line[:len(line)-1]   # 맨 뒤 엔터키를 삭제(안 하면 매줄마다 엔터키가 두개씩 삽입되기 때문)
    print(line)
f.close()

# with : 자원을 사용하고 자동 반납
#        close를 하지 않아도 자동처리해줌
with open("test.txt", "r", encoding="utf-8") as f:
    line = f.readlines()
    for line in lines:
        line = line[:len(line)-1]
        print(line)

# 한 줄씩 읽어서 처리하기 : 용량이 너무 커서 한꺼번에 다 읽어올 수 없을 때 사용(굳이 구분을 하진 않는듯??)
with open("test.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line!="":         # 더이상 읽을 게 없을 때까지 읽어와서
        print(line[:len(line)-1])   # 출력
        line = f.readline()


