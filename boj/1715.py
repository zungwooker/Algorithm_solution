import sys, heapq
N = int(sys.stdin.readline().rstrip())
bundles = []
result = 0

for _ in range(N):
    heapq.heappush(bundles, int(sys.stdin.readline().rstrip()))

if N==1:
    print(0)
    sys.exit()

while len(bundles) != 1:
    a = heapq.heappop(bundles)
    b = heapq.heappop(bundles)
    result += a+b
    heapq.heappush(bundles, a+b)

print(result)
