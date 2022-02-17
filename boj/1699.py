N = int(input())
if N<4:
    print(N)
    exit()

dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(2, int((N+1)/2) + 1):
    if i*i <= N:
        dp[i*i] = 1

if dp[N] == 1:
    print(1)
    exit()

last = 4
for i in range(5, N+1):
    if dp[i] == 1:
        last = i
    else:
        


print(dp[N])