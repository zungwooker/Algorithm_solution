N = int(input())
milk = list(map(int, input().split()))

toRight = 0
RCount = 0
toLeft = 0
LCount = 0
for i in milk:
    if i == toRight:
        RCount += 1
        toRight = (toRight+1)%3

milk.reverse()
for i in milk:
    if i == toLeft:
        LCount += 1
        toLeft = (toLeft+1)%3

print(max(RCount, LCount))
print(RCount, LCount)