# dict 안에 list 담기

score = {
    "name":["홍길동","김길동","이길동","박길동","최길동"],
    "kor":[90,80,70,60,50],
    "mat":[90,80,70,60,50],
    "eng":[90,80,70,60,50]
}

print(score["name"][0])
print(score["name"][1])
print(score["name"][2])
print(score["name"][3])
print(score["name"][4])

print(score["kor"][0])
print(score["kor"][1])
print(score["kor"][2])
print(score["kor"][3])
print(score["kor"][4])

# 총점 필드를 score["필드명"]로 저장
score["total"] = list()     #score["total"]=[]

score["total"].append(score["kor"][0] + score["eng"][0] + score["mat"][0])
score["total"].append(score["kor"][1] + score["eng"][1] + score["mat"][1])
score["total"].append(score["kor"][2] + score["eng"][2] + score["mat"][2])
score["total"].append(score["kor"][3] + score["eng"][3] + score["mat"][3])
score["total"].append(score["kor"][4] + score["eng"][4] + score["mat"][4])

print(score)

# list 안에 dict 담기
score = [
    {"name":"홍길동", "kor":90, "mat":80, "eng":70},
    {"name":"김길동", "kor":80, "mat":70, "eng":60},
    {"name":"이길동", "kor":70, "mat":60, "eng":50},
    {"name":"박길동", "kor":60, "mat":50, "eng":40},
    {"name":"최길동", "kor":50, "mat":40, "eng":30}
]
print(score[0]["name"],score[0]["kor"],score[0]["mat"],score[0]["eng"])

for i in range(0, len(score)):
    print(score[i]["name"], score[i]["kor"], score[i]["mat"], score[i]["eng"])

for s in score:
        print(s["name"], s["kor"], s["mat"], s["eng"])

