import sys, heapq
N = int(sys.stdin.readline().rstrip())
arr = []
negCount = 0
zeroCount = 0
oneCount = 0
result = 0

# 데이터 입력받으며 카운트
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num<0:
        negCount += 1
    elif num==0:
        zeroCount += 1
    elif num==1:
        oneCount += 1

    heapq.heappush(arr, num)

# 음수 관리하기
for _ in range(int(negCount/2)):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    result += a*b
if negCount%2==1:
    if zeroCount>0: # 0이 있다면 0과 곱하여 음수 1개를 제거
        zeroCount -= 1
        heapq.heappop(arr) # 음수 pop
        heapq.heappop(arr) # 0 pop
    else: # 0이 없다면 음수를 결과값에 더함
        result += heapq.heappop(arr) # 음수 결과값에 더하고 pop

# 0과 1 관리하기
# 1의 갯수만큼 결과값에 더하고 0과 1의 개수만큼 pop
result += oneCount

for _ in range(oneCount+zeroCount):
    heapq.heappop(arr)

if len(arr)%2==1:
    result += heapq.heappop(arr)

while len(arr) != 0:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        result += a*b

print(result)