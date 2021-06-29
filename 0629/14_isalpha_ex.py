strings=input("문장을 입력하세요 : ")
alpha,digit,space,etc=0,0,0,0
for s in strings:
    if s.isalpha():
        alpha=alpha+1
    elif s.isdigit():
        digit=digit+1
    elif s.isspace():
        space=space+1
    else:
        etc+=1
print("알파벳 : {}개".format(alpha))
print("숫자 : {}개".format(digit))
print("스페이스 : {}개".format(space))
print("기타 : {}개".format(etc))
