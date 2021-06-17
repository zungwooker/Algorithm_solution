N = int(input())
ropes = []
maxWeight = 0

for _ in range(N):
    ropes.append(int(input()))

ropes.sort()

for i in range(N):
    if maxWeight < ropes[i]*(N-i):
        maxWeight = ropes[i]*(N-i)

print(maxWeight)


# 조금 더 빠른 알고리즘

"""
import sys

N = int(sys.stdin.readline().rstrip())
maxWeight, numOfRopes = 0, 0
ropes = [0]*10001

for _ in range(N):
    ropes[int(sys.stdin.readline().rstrip())] += 1

for i in range(10000, 0, -1):
    # i는 로프의 길이
    numOfRopes += ropes[i]
    maxWeight = max(maxWeight, numOfRopes*i)

print(maxWeight)
"""