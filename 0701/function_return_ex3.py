def order(a,b):
    result = a*b
    return result

a=int(input("상품가격 입력 : "))
b=int(input("주문수량 입력 : "))
print("----------------------")
print("상품가격 : {}원".format(a))
print("주문수량 : {}개".format(b))
print("주문액 : {}원".format(order(a,b)))
