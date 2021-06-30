list=[]
for i in range(5):
    score=int(input("학생{} 점수 입력 : ".format(i+1)))
    list.append(score)
sum=sum(list)
avg=sum/len(list)
print("총점 : {}".format(sum))
print("총점 : {}".format(avg))
