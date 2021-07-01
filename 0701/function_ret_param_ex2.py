def get_interest(a,b):
    result = format(int(a*b/100),",")
    return result

a=int(input("예금액 입력 : "))
b=float(input("이자율 입력(%) : "))
print("이자액 : {}원".format(get_interest(a,b)))
