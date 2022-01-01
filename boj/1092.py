N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxs = list(map(int, input().split()))

if min(cranes) > max(boxs):
    print(M//N+1)
    exit()
elif max(cranes) < max(boxs):
    print(-1)
    exit()

cranes.sort(reverse=True)
boxs.sort(reverse=True)
craneDuty = [0 for _ in range(N)]


