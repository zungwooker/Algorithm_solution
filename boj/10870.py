nums = [0 for _ in range(21)]
nums[1] = 1
n = int(input())
for i in range(2, n+1):
    nums[i] = nums[i-1] + nums[i-2]
print(nums[n])