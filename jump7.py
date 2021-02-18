i =1
while i < 101:
    if i%7==0:
        pass
    elif i%10==7:
        pass
    elif i//7==10:
        continue
    else:
        print(i,end="")
    i+=1

