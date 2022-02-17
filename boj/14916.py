n = int(input())
if n == 1 or n == 3:
    print(-1)
    exit()

if n%5 == 0:
    print(n//5)
elif n%2 == 1:
    print(1+((n-5)//10)*2+((n-5)%10)//2)
else:
    print((n//10)*2+(n%10)//2)