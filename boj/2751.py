import heapq
import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    heapq.heappush(li, int(input()))
for _ in range(N):
    print(heapq.heappop(li))
