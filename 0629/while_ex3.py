while True:
    n=input("숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요:")
    if n=='x':
        print("종료합니다")
        break
    else:
        if int(n)%2==0:
            continue
        else:
            print("{}는 홀수입니다.".format(n))
