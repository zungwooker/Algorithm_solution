import math
n,m = map(int, input().split())

result = 1
for i in range(1, n+1):
    result = int(result * i)

for i in range(1, m+1):
    result = int(result/i)

for i in range(1, n-m+1):
    result = int(result/i)

print(result)

up = math.factorial(n)
down = (math.factorial(n - m)) * (math.factorial(m))

print(up // down)