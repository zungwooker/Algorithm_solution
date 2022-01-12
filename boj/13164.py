N, K = map(int, input().split())
students = list(map(int, input().split()))
diff = []
for i in range(N-1):
    diff.append(students[i+1] - students[i])

diff.sort()
for _ in range(K-1):
    diff.pop()

print(sum(diff))