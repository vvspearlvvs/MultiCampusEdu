n=int(input("학생 수 입력 : "))
list=[]
cnt=0
for i in range(n):
    score=int(input("학생{} 점수 입력 : ".format(i+1)))
    list.append(score)
sum=sum(list)
avg=sum/len(list)
print("총점 : {}".format(sum))
print("총점 : {}".format(avg))
for s in list:
    if s>=80:
        cnt=cnt+1
print("80점 이상 학생 : {}명".format(cnt))
