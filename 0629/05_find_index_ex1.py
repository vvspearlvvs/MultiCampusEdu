input=input("이메일 입력 : ")
email=input.split("@").split()

if '@' not in email:
    print("이메일 형식이 아닙니다.")
else:
    email=email.split("@")[1]
    print(email)
    if '.' not in email:
        print("이메일 형식이 아닙니다.")
    else:
        email=email.split(".")
        print(email)
