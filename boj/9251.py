st1, st2 = ' '+input(), ' '+input()

dp = [[0 for _ in range(len(st1))] for _ in range(len(st2))]

for i in range(1, len(st2)):
    for j in range(1, len(st1)):
        if st2[i] == st1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])