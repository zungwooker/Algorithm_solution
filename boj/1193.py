x = float(input())
i = int(-(-((8*x+1)**.5-1)//2))
if i%2 == 0:
    up = int((i - (i*i) + 2*x)/2)
    print(str(up) + "/" + str(i+1-up))
else:
    up = int((i + (i*i) + 2 - 2*x)/2)
    print(str(up) + "/" + str(i+1-up))

