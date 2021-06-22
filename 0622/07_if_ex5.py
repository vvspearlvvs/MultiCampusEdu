type=int(input("도형 입력(1: 사각형, 2: 삼각형, 3:원) : "))
if type == 1:
    x=int(input("가로 입력 : "))
    y=int(input("세로 입력 : "))
    print("사각형의 면적 = ",str(x*y))
elif type == 2:
    a=int(input("밑면 입력 : "))
    h=int(input("높이 입력 : "))
    print("삼각형의 면적 = ",str((a*h)/2))
elif type == 3:
    r=int(input("반지름 입력 : "))
    print("원의 면적 = ",str(3.14*r**2))
