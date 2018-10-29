score=list()
total=0
inscore=0

while (inscore!=-1):
    inscore=int(input('請輸入數字,-1離開'))
    score.append(inscore)
    if (inscore==-1):
        break

for item in score:
    total=total+item

avg=total/len(score)
print("成績總和:{}".format(total))
print("成績平均:{}".format(avg))


