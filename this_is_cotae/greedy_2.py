n, m = map(int, input().split())
arr = []
min = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    arr[i].sort()
    if min<arr[i][0]:
        min = arr[i][0]

print(min)