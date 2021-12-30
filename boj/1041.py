N = int(input())
nums = list(map(int, input().split()))

if N==1:
    print(sum(nums)-max(nums))
    exit()

minIdx1 = 0 # 가장 작은 수
minIdx2 = 0 
minIdx3 = 0
minNum = min(nums)

for i in range(6):
    if minNum == nums[i]:
        minIdx1 = i

        nextMinNum = max(nums)
        for j in range(6):
            if j != i and j != 5-i and nextMinNum >= nums[j]:
                minIdx2 = j
                nextMinNum = nums[j]
        
        nextMinNum = max(nums)
        for j in range(6):
            if j != minIdx1 and j != minIdx2 and j != 5-minIdx1 and j != 5-minIdx2 and nextMinNum >= nums[j]:
                minIdx3 = j
                nextMinNum = nums[j]
        
        break

if N==2:
    print((nums[minIdx1]+nums[minIdx2]+nums[minIdx3])*8 - nums[minIdx3]*4)
else:
    print((nums[minIdx1]+nums[minIdx2]+nums[minIdx3])*4 + (nums[minIdx1]+nums[minIdx2])*(8*N-12) + nums[minIdx1]*((N-2)**2+(N-1)*(N-2)*4))




