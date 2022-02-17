nums = list(map(int, input().rstrip()))
if sum(nums)%3 != 0 or 0 not in nums:
    print(-1)
    exit()
nums.sort(reverse=True)
for n in nums:
    print(n, sep='', end='')
