# while : 한번도 수행되지 않을 가능성이 있을 때
# 한 번 이상 수행될 때(Python에는 존재하지 않음) : do, switch
# for : 몇 번 수행할지 알 수 있을 때

i = 1
while i<10:
    print(i)
    i = i+1

# 정수 하나를 입력받아 합계/ 평균을 구함
# 마지막에 음수가 입력되면 멈춤
dataList=[]
i=int(input("정수를 입력하세요 : "))
while i>=0:
     dataList.append(i)
     i=int(input("정수를 입력하세요 : "))

print(sum(dataList))
print(sum(dataList)/len(dataList))