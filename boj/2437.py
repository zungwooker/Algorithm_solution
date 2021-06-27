import sys

N = int(sys.stdin.readline().rstrip())
maxWeight = 0
weights = list(map(int, sys.stdin.readline().rstrip().split()))
weights.sort()

if weights[0]>1:
    print(1)
    sys.exit()

for i in range(N):
    if maxWeight==weights[i] or maxWeight>weights[i] or maxWeight+1==weights[i]:
        maxWeight += weights[i]
    else:
        print(maxWeight+1)
        sys.exit()

print(maxWeight+1)