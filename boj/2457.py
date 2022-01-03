N = int(input())
flowers = []
selected = []
for i in range(N):
    flowers.append(list(map(int, input().split())))
    if flowers[i][0] <= 2:
        flowers[i][0] = 3
        flowers[i][1] = 1
    if flowers[i][2] == 12:
        flowers[i][3] = 1
    
selected.append(flowers[0])
for flower in flowers[1:]:
    if flower[2] >= selected[-1][2] or 

