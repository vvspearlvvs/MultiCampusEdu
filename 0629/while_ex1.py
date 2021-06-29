money=10000
song=2000
i=0
while money!=0:
    i=i+1
    print("노래를 "+str(i)+"곡 불렀습니다.")
    money=money-song
    print("현재 "+str(money)+"원 남았습니다")

print("잔액이 없습니다.종료합니다.")
