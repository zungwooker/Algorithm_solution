import sys
input = sys.stdin.readline

mod = 1000000009
t = int(input())
nums = []

for _ in range(t):
    nums.append(int(input()))
dp = [[0,0,0,0] for _ in range(max(nums) + 1)]

dp[1] = [0,1,0,0] 
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]

for i in range(4, max(nums) + 1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%mod
    dp[i][2] = (dp[i-2][1] + dp[i-2][3])%mod
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%mod

for num in nums:
    print(sum(dp[num])%mod)