def order(a,b):
    qty = a*b #주문액
    if qty >=100000:
        discount = qty*0.1 #10%할인
    elif qty >=50000:
        discount = qty*0.05 #5%할인
    else:
        discount = 0
    total = qty-(discount) #지불액
    return qty,discount,total

price=int(input("상품가격 입력 : "))
amount=int(input("주문수량 입력 : "))
print("----------------------")
qty = order (price,amount)[0]
discount = order (price,amount)[1]
total = order (price,amount)[2]
print("주문액 : {}원".format(qty))
print("할인액 : {}원".format(discount))
print("지불액 : {}원".format(total))
