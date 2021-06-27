result = 1
nums = [0 for _ in range(10)]
for _ in range(3):
    result *= int(input())

for i in str(result):
    nums[int(i)] += 1

for i in nums:
    print(i)