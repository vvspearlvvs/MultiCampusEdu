a=int(input("숫자1 입력 : "))
b=int(input("숫자2 입력 : "))
sum=0
for i in range(a,b+1):
    sum=sum+i
print(str(a)+"부터 "+str(b)+"까지의 합 : "+str(sum))
