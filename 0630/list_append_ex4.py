list=[]
while True:
    item=input("상품 등록 (엔터키 누르면 종료) : ")
    list.append(item)
    if item == "":
        break
print("등록된 상품 : {}".format(' '.join(list)))
