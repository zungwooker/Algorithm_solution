N = (int(input())//100)*100
F = int(input())
c = N%F

if c:
    if F-c>9:
        print(F-c)
    else:
        print(0, F-c, sep='')
else:
    print("00")
