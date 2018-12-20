from flask import Flask, render_template, request
import random
import requests
import json
from faker import Faker 


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/lotto')
def lotto():
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res) #가져올 정보들을 dict형태로 넣어줌
    print(lotto_dict["drwNoDate"]) #키값은 스트링형태로 "", 접근할때는 [대괄호]
    

    
    # 직관적인 for문 작성
    week_num = [] #여러개의 숫자를 한번에 보내주기 위해
    week_format_num=[]
    drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
    num_list = range(1,46)
    pick = random.sample(num_list, 6)
    pick = [2, 25, 28, 30, 33, 6]
    
    for num in drwtNo:
        number = lotto_dict[num] #첫번째 for문에서는 lotto_dict["drwtNo1"]을 참조해줌..
        week_num.append(number) #append for문을 반복하며 나오는 숫자를 붙여넣기
        #print(week_num) #여기서 완성된 마지막 한줄만 사용
        
    bnusNo = lotto_dict["bnusNo"]
    list[0] = "bnusNo"
    
    inter = list(set(pick).intersection(week_num))
    a = len(inter)
    
    interbonus = list(set(pick).intersection(list))
    b = len(interbonus)
    
    if a == 6:
        x = "1등입니다"
    elif a == 5:
        if b == 1:
            x = "2등입니다"
        else:
            x = "3등입니다"
    elif a == 4:
        x = "4등입니다"
    elif a == 3:
        x = "5등입니다"
    else:
        x = "꽝"
       
    #pick = 우리가 생성한 번호
    #week_num = 이번주 당첨번호
    ### 위의 두 값을 비교해서 로또 당첨 등수출력
    # 1등 : 6개의 숫자를 다 맞출 때
    # 2등 : 5개의 숫자를 다 맞출 때 + 보너스번호
    # 3등 : 5개의 숫자
    # 4등 : 4개의 숫자
    # 5등 : 3개

    # return render_template("lotto.html", lotto=pick, lottery=lottery)
    return render_template("lotto.html", lotto=pick, week_num=week_num, a=a, x=x)
    


@app.route('/lottery')
def lottery():
    # 로또 정보를 가져온다. & 필요한 것만 고른다.
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    
    #1등 당첨번호를 week 리스트에 넣는다.
    week = []
    for i in range(1,7): # 1부터 6까지, range(6)은 0부터 6까지임
        num = lotto_dict["drwtNo{}".format(i)]
        week.append(num)
        
    # 보너스 번호를 bonus 변수에 넣는다.
    bnus = lotto_dict["bnusNo"]
    
    # 임의의 로또번호를 생성한다.
    pick = random.sample(range(1,46),6)
    
    # 비교해서 몇등인지 저장한다.
    match = len(set(pick) & set(week)) # 두 set를 비교함
    
    if match==6:
        text = "1등"
    elif match==5:
        if bonus in pick:
            text = "2등"
        else:
            text = "3등"
    elif match==4:
        text = "4등"
    else:
        text = "꽝"
    

    # 집합자료형 set -> 중복을 허용하지 않고 순서가 없음.
    
    # 사용자에게 데이터를 넘겨준다.
    
    return render_template("lottery.html", pick=pick, week=week, text=text)



@app.route('/ping') #데이터입력
def ping():
    return render_template("ping.html")
    
@app.route('/pong') #데이터출력
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_road = fake.road()
    fake_day = fake.day_of_week()
    return render_template("pong.html", html_name=input_name, fake_road=fake_road, fake_day=fake_day)
    
    