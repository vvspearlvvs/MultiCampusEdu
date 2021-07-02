dict={}
while True:
    en = input("영어 단어 등록 :")
    if en =="quit":
        break

    if en in dict:
        print("{}는 이미 등록된 단어입니다".format(en))
        print()
    else:
        ko = input("{}의 뜻입력 : ".format(en))
        dict[en]=ko
        print()
print("-----------------------------")
while True:
    en = input("검색할 단어 입력  :")
    if en =="quit":
        break

    if en not in dict:
        print("{}는 사전에 없는 단어입니다".format(en))
        print()
    else:
        print("{}의 뜻은 {}입니다".format(en,dict[en]))
        print()
