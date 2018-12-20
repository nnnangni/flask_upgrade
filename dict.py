phonebook = {
    "치킨집":"02-000-0000", 
    "피자집":"062-123-4567"
}
print(phonebook["치킨집"])

# 가수 그룹의 딕셔너리를 만들어주세요
# 변수명 : 그룹이름
# key : 이름
# value : 나이(가상)

exo = {
    "수호":28,
    "찬열":27,
    "카이":25,
    "디오":26,
    "백현":27,
    "세훈":25,
    "시우민":29,
    "첸":27,
    "레이":28
}

btob = {
    "서은광":29,
    "이민혁":29,
    "이창섭":28,
    "임현식":27,
    "프니엘":26,
    "정일훈":25,
    "육성재":24
}

idol ={
    "exo":exo,
    "btob":btob
}

print(idol)
#print(idol["exo"]["디오"])

# score = {
#     "수학":50,
#     "국어":70,
#     "영어":100
# }

# for key, value in score.items():
#     pass
#     # print(key)
#     # print(value)

# for key in score.keys():
#     print(key)
    
# for value in score.values():
#     print(value)

# score_sum = 0
# for value in score.values():
#     score_sum = score_sum + value
# print(score_sum/3)

ssafy language python python standard library


for value in ssafy["language"]["python"]["python standard library"]():
    if requests 

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}




# 1. ssafy를 진행하는 지역(location)은 몇개인가요?

print(len(ssafy["location"]))


# 2. python standard library에 'requests'가 있나요? (t,f)



# 3. gj1반의 반장의 이름을 출력하세요.


print(ssafy["classes"]["gj1"]["class president"])


# 4. ssafy에서 배우는 언어들을 출력하세요(dictionary.keys활용)



# 5. ssafy gj2의 강사와 매니저의이름을출력하세요
#예시) teacher2
#      pro2


#6. framework들의 이름과 설명을 다음과 같이 출력하세요.