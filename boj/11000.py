import sys, heapq

N = int(sys.stdin.readline().rstrip())
Lessons = []
EndTimeTable = [1]

# 수업 정보를 받고 수업을 시작과 끝나는 순으로 정렬
for _ in range(N):
    Lessons.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
Lessons.sort(key=lambda x:(x[0], x[1]))

# 수업들 순서대로 검사 후 입력
for lesson in Lessons:
    t = heapq.heappop(EndTimeTable)
    if t > lesson[0]:
        heapq.heappush(EndTimeTable, t)
    heapq.heappush(EndTimeTable, lesson[1]) 
        
print(len(EndTimeTable))


