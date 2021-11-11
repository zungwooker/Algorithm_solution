import math
n,m = map(int, input().split())

result = 1
apap = 0
for i in range(1, n+1):
    result = result * i

apap = result

for i in range(1, m+1):
    result = result/i
    apap = int(apap/i)

for i in range(1, n-m+1):
    result = result/i
    apap = int(apap/i)
    if apap-result != 0:
        print(apap, result, i, result*i)

print(result)

up = math.factorial(n)
down = (math.factorial(n - m)) * (math.factorial(m))

print(up / down)

print(9330691110047998.0 / 7)

