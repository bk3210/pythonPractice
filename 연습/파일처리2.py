with open("test2.txt", "w", encoding="utf-8") as f:
    line = input("아무거나 입력해 보세요")
    while line!="":
       print(line, file=f)  # 출력한 내용이 파일로 보내짐
       line = input("아무거나 입력해")

with open("test2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines() 
    print(lines)