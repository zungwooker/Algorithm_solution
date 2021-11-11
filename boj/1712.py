a,b,c = map(int, input().split())

sumOfCost = a
profit = 0

if b>=c:
    print(-1)
    exit()

print(int(-(a/(b-c))+1))