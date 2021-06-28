N, M = map(int, input().split())

if N==1:
    print(1)
elif N==2:
    if M<7:
        print(int((M+1)/2))
    else:
        print(4)
else:
    if M<5:
        print(M)
    elif M<7:
        print(4)
    else:
        print(M-2)