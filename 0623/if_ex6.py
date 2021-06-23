print("###### 상품 정보 #######")
print("1 노트북 : 1,200,000 원")
print("2 디지털카메라 : 400,000 원")
print("#######################")

PRICE1=1200000
PRICE2=400000
def result(item,amount,price,order):
    print("###### 주문 내용 #######")
    if order >=1000000:
        discount = int(order*0.1)
    elif order <1000000 and order >=500000:
        discount = int(order*0.05)
    else:
        discount = 0
    print("상품명 :    ",item)
    print("가격 :      ",format(price,","),"원")
    print("주문 수량 : ",amount)
    print("주문액 :    ",format(order,","),"원")
    print("할인액 :    ",format(discount,","),"원")
    print("총지불액 :  ",format(order-discount,","),"원")

num=int(input("상품번호 입력 : "))
if num ==1:
    amount=int(input("주문 수량 입력 : "))
    result("노트북",amount,PRICE1,PRICE1*amount)
elif num ==2:
    amount=int(input("주문 수량 입력 : "))
    result("디지털카메라",amount,PRICE2,PRICE2*amount)
else:
    print("잘못 입력하였습니다. 종료합니다.")
