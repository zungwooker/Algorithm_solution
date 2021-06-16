N = int(input())

five = N//5
rest = N%5

# 3<=N<=5000
if rest==0:
    print(five)
elif rest==1:
    print(five+1)
elif rest==2:
    if N==7:
        print(-1)
    else:
        print(five+2)
elif rest==3:
    print(five+1)
elif rest==4:
    if N==4:
        print(-1)
    else:
        print(five+2)