N = int(input())
stairs = []
result = [0 for _ in range(N)]
for _ in range(N):
    stairs.append(int(input()))

if N<3:
    print(sum(stairs))
    exit()

result[0] = stairs[0]
result[1] = stairs[0] + stairs[1]
result[2] = max(stairs[0], stairs[1]) + stairs[2]

for i in range(3, N):
    result[i] = max(result[i-2], (result[i-3] + stairs[i-1])) + stairs[i]

print(result[-1])