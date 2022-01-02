N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxs = list(map(int, input().split()))

if min(cranes) > max(boxs):
    print(-(-M//N))
    exit()
elif max(cranes) < max(boxs):
    print(-1)
    exit()

cranes.sort()
boxs.sort()
craneDuty = [0 for _ in range(N)]

i = 0 # for crane
j = 0 # for box
leftBoxs = M
movedBoxs = 0

leftCranes = N
doneCranes = 0
ceiling = (leftBoxs - movedBoxs) / (leftCranes - doneCranes)

while j < M:
    if cranes[i] >= boxs[j] and craneDuty[i] < ceiling:
        craneDuty[i] += 1
        j += 1
        movedBoxs += 1
    else:
        i += 1
        doneCranes += 1
        ceiling = (leftBoxs - movedBoxs) / (leftCranes - doneCranes)

print(max(craneDuty))