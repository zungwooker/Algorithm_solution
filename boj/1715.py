import sys, heapq
N = int(sys.stdin.readline().rstrip())
bundles = []
result = 0

for _ in range(N):
    heapq.heappush(bundles, int(sys.stdin.readline().rstrip()))

if N==1:
    print(0)
    sys.exit()

while len(bundles) != 1: # O(NlogN)
    a = heapq.heappop(bundles) # 1
    b = heapq.heappop(bundles) # 1
    result += a+b # 1
    heapq.heappush(bundles, a+b) # logN

print(result)
