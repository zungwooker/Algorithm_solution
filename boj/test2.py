import heapq
appeared = {1:10, 2:30, 5:1, 3:-1}
heapq.heapify(appeared)
print(heapq.heappop(appeared))
