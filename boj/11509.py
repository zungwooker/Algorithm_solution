import sys
N = int(sys.stdin.readline())
balloons = list(map(int, sys.stdin.readline().split()))

arrows = [0 for _ in range(1000000)]
arrowsNum = 0
for x in balloons:
    if arrows[x]:
        arrows[x] -= 1
        arrows[x-1] += 1
    else:
        arrows[x-1] += 1
        arrowsNum += 1

print(arrowsNum)