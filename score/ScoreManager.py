from ScoreData import ScoreData
import pickle

class ScoreManager:
    dataList = list()
    
    def __init__(self):
        self.load()
        # self.dataList.append(ScoreData("A", 100, 100, 100))
        # self.dataList.append(ScoreData("B", 90, 90, 90))
        # self.dataList.append(ScoreData("C", 80, 80, 80))
        # self.dataList.append(ScoreData("D", 70, 70, 70))
        # self.dataList.append(ScoreData("E", 60, 60, 60))

    def append(self):
        sd = ScoreData()
        sd.name = input("이름 : ")
        sd.kor = int(input("국어 : "))
        sd.mat = int(input("수학 : "))
        sd.eng = int(input("영어 : "))
        sd.process()
        self.dataList.append(sd)

    def output(self):
        for item in self.dataList:
            item.display()
    
    def search(self):
        e = input("이름을 입력하세요 : ")
        # filter(람다식, 리스트)
        # filter 함수에 전달할 람다식은 반환값이 True/False
        # filter에 전달되는 람다함수는 데이터 요소를 파라미터로 하여 요소마다 호출
        for item in filter(lambda x: x.name == e, self.dataList):
            item.display()
            find = True
        if find==False:
            print("검색 결과가 없습니다.")

    def modify(self):
        name = input("수정할 이름을 입력하세요 : ")
        modifyList = list(filter(lambda x : x.name == name, self.dataList))
        if len(modifyList)==0:     # 한명도 값이 들어가지 않았을 때
            print("존재하지 않는 이름입니다.")
            return  # 함수 종료
        i=1
        for item in modifyList:
            print("{}번째 : ".format(i))
            item.display()
            i+=1

        pos = int(input("수정할 항목 번호를 선택하세요 : "))
        if pos<0 or pos>len(modifyList):
            print("잘못 선택하셨습니다.")
            return
        
        modifyList[pos-1].name = input("이름 : ")
        modifyList[pos-1].kor = int(input("국어 : "))
        modifyList[pos-1].mat = int(input("수학 : "))
        modifyList[pos-1].eng = int(input("영어 : "))
        modifyList[pos-1].process()
        print("수정이 완료되었습니다.")

    def delete(self):
        name = input("삭제할 이름을 입력하세요 : ")
        deleteList = list(filter(lambda x : x.name == name, self.dataList))
        if len(deleteList)==0:
            print("존재하지 않는 이름입니다.")
            return
        
        i=1
        for item in deleteList:
            print("{}번째 : ".format(i))
            item.display()
            i+=1

        pos = int(input("삭제할 항목 번호를 선택하세요 : "))
        if pos<0 or pos>len(deleteList):
            print("잘못 선택하셨습니다.")
            return
        
        # 삭제할 참조의 주소를 가져옴
        deleteItem = deleteList[pos-1]  # 삭제대상이 되는 참조를 가져온다
        self.dataList.remove(deleteItem)
        print("삭제되었습니다.")
    
    def sort(self):
        sortedDataList = sorted(self.dataList, key=lambda item:item.name, reverse=True)
        for item in sortedDataList:
            item.display()
    
    # 데이터파일 저장
    def save(self):
        # 파일 쓰기모드
        f = open("score.txt", "w", encoding="utf-8")
        for item in self.dataList:
            print("{} {} {} {}".format(item.name, item.kor, item.mat, item.eng), file=f)
        f.close()

    # 데이터 불러오기
    def load(self):
        self.dataList = list()  # 불러오기할 때는 기존 데이터를 삭제 - 새로운 객체 생성
        f = open("score.txt", "r", encoding="utf-8")
        line = f.readline() # 한줄씩 읽기, 공백을 기준으로 토큰 분리
        while line!="" :
            tokens = line.split(" ")
            data = ScoreData()
            data.name = tokens[0]
            data.kor = int(tokens[1])
            data.mat = int(tokens[2])
            data.eng = int(tokens[3])
            data.process()
            self.dataList.append(data)
            line = f.readline() # 다음줄을 읽는다
        f.close()

    # pickle 데이터 저장
    def save2(self):
        f = open("score.bin", "wb", encoding="utf-8")
        pickle.dump(self.dataList, f=f)
        f.close()

    # pickle 데이터 불러오기
    def load2(self):
        f = open("score.bin", "rb")
        self.dataList = pickle.load(f=f)
        f.close()


    def menuDisplay(self):
        print("1. 추가")
        print("2. 출력")
        print("3. 검색")    # filter 
        print("4. 수정")    # filter
        print("5. 삭제")    # filter   
        print("6. 정렬")    # sorted
        print("7. 저장")    # 결과만 저장
        print("8. 불러오기")    # load
        print("9. 피클 저장")
        print("10. 피클 불러오기")
        print("0. 종료")

    def start(self):
        while True:
            self.menuDisplay()
            sel = input("선택 : ")
            if sel == "1":
                self.append()
            elif sel=="2":
                self.output()
            elif sel=="3":
                self.search()
            elif sel=="4":
                self.modify()
            elif sel=="5":
                self.delete()
            elif sel=="6":
                self.sort()
            elif sel=="7":
                self.save()
            elif sel=="8":
                self.load()
            elif sel=="9":
                self.save2()
            elif sel=="10":
                self.load2()
            elif sel=="0":
                print("프로그램 종료")
                return
            
            
if __name__ == "__main__":
    sm = ScoreManager()
    sm.start()