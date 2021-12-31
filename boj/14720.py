N = int(input())
milk = list(map(int, input().split()))

toRight = 0
RCount = 0
for i in milk:
    if i == toRight:
        RCount += 1
        toRight = (toRight+1)%3

print(RCount)