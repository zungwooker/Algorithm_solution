import math
box = list(map(int, input().split()))
N = int(input())
box.sort()
cbs = []
for _ in range(N):
    cb = list(map(int, input().split()))
    cb = [int(math.pow(2,cb[0])), cb[1]]
    if box[0] > cb[0]:
        cbs.append(cb)
