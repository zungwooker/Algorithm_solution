"""
import sys

R, C = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(R):
    maps.append(list(sys.stdin.readline().rstrip()))

counts = 0
for i in range(R):
    arrived = True
    vis = []
    r = i

    j = 1
    while j<C:
        if r>0 and j>1 and maps[r-1][j-1]=='.':
            r = r-1
            vis.append((r,j))
            continue
        if r>0 and maps[r-1][j]=='.': # 위로
            r = r-1
            vis.append((r,j))
            j += 1
            continue
        if maps[r][j]=='.': # 앞으로
            vis.append((r,j))
            j += 1
            continue
        if r+1<R and maps[r+1][j]=='.': # 아래로
            r = r+1
            vis.append((r,j))
            j += 1
            continue
        arrived=False
        break

    if arrived==True:
        counts += 1
        for k in vis:
            maps[k[0]][k[1]] = 'x'

print(counts)

"""