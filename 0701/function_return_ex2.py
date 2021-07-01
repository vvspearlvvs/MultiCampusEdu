def get_area(a,b):
    result = a*b
    return result

a=int(input("가로길이 입력 : "))
b=int(input("세로길이 입력 : "))
print("사각형의 면적 : {}".format(get_area(a,b)))
