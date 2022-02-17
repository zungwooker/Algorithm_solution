n, m = map(int, input().split())

pascal = [[] for _ in range(n+2)]
pascal[0] = [0]
pascal[1] = [1]
pascal[2] = [1, 1]

for i in range(3, n+1):
    pascal[i].append(1)
    for j in range(i-2):
        pascal[i].append(pascal[i-1][j]+pascal[i-1][j+1])
    pascal[i].append(1)

print(pascal[n][m-1])