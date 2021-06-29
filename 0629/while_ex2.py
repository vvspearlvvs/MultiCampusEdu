n=int(input("마지막 숫자를 입력하세요:"))
sum=0
i=0
while i!=n:
    i=i+1
    if i%2==0:
        continue
    else:
        sum=sum+i


print("1부터 "+str(n)+"까지의 홀수의 합은 "+str(sum)+" 입니다.")
