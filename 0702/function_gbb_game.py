import random

def gbb_game(you,com):
    if com > you :
        print("컴퓨터가 이겼습니다.")
    elif com < you :
        print("당신이 이겼습니다.")
    else:
        print("비겼습니다.")
while True:
    you = int(input("YOU 입력 (1:가위, 2:바위, 3:보) : "))
    com = random.randint(1,3)
    gbb_game(you,com)
    print("COM : ",str(com))
