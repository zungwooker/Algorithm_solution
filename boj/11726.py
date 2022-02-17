n = int(input())
methods = [0 for _ in range(1001)]

methods[0] = 0
methods[1] = 1
methods[2] = 2
methods[3] = 3
for i in range(4, n+1):
    methods[i] = methods[i-1] + methods[i-2]

print(methods[n]%10007)
