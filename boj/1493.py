import math

def maxCubes(box, side):
    return int((box[0]//side)*(box[1]//side)*(box[2]//side))

box = list(map(int, input().split()))
N = int(input())
cubeLimit = min(box)

cbs = []
for _ in range(N): # box에 들어갈 수 있는 크기의 cube만 cbs에 저장
    cb = list(map(int, input().split()))
    side = math.pow(2,cb[0])
    if cubeLimit >= side: # 한 개라도 들어갈 수 있는 큐브
        cbs.append([int(math.pow(2,cb[0]*3)), cb[1], maxCubes(box,side)]) # cbs[i][0] == 큐브의 부피, [1] == 큐브의 재고, [2] == 사용 가능 최대 큐브 수

boxVolume = box[0]*box[1]*box[2]
if maxCubes(box, int(math.pow(cbs[0][0], 1/3)))*cbs[0][0] != boxVolume: # 충분한 개수의 가장 작은 큐브로만 채워도 불가한 경우
    print(-1)
    exit()

usedCubes = 0
cubeNeed = [0 for _ in range(len(cbs))]
cubeMod = [0 for _ in range(len(cbs))]

cubeNeed[0] = int(boxVolume//cbs[0][0])
for i in range(len(cbs)-1): # 큐브의 개수가 무한한 상태에서 최선으로 큐브를 넣은 상황
    cubeNeed[i+1] = int(cubeNeed[i]//(int(cbs[i+1][0]//cbs[i][0])))
    cubeNeed[i] = int(cubeNeed[i]%(int(cbs[i+1][0]//cbs[i][0]))) # 다음 크기의 큐브로 최대로 많이 전환후에 남는 큐브 수, int(cbs[i+1][0]//cbs[i][0]) == 다음 큐브로 만들기 위해 필요한 현재 큐브 수
    if cubeNeed[i+1] > cbs[i+1][2]:
        cubeNeed[i] += (cubeNeed[i+1]-cbs[i+1][2])*(int(cbs[i+1][0]//cbs[i][0]))
        cubeNeed[i+1] = cbs[i+1][2]

for i in range(len(cbs)-1, 0, -1):
    if cubeNeed[i] > cbs[i][1]:
        cubeNeed[i-1] += (cubeNeed[i]-cbs[i][1])*(int(cbs[i][0]//cbs[i-1][0]))
        cubeNeed[i] = cbs[i][1]

if cubeNeed[0] > cbs[0][1]:
    print(-1)
else:
    print(sum(cubeNeed))
