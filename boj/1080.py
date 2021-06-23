import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A, B, C= [], [], [[] for _ in range(N)]
counts = 0

for _ in range(N): # A 입력
    A.append(sys.stdin.readline().rstrip())

for _ in range(N): # B 입력
    B.append(sys.stdin.readline().rstrip())

for i in range(N): # A와 B가 서로 다르면 1, 같으면 0을 C에 기록
    for j in range(M):
        if A[i][j]!=B[i][j]:
            C[i].append(1)
        else:
            C[i].append(0)
        
for i in range(N-2):
    for j in range(M-2):
        if C[i][j]%2==1:
            counts += 1
            for x in range(3):
                for y in range(3):
                    C[i+x][j+y] += 1
    for j in range(M):
        if C[i][j]%2==1:
            print(-1)
            sys.exit()


for i in range(N-2, N):
    for j in range(M):
        if C[i][j]%2==1:
            print(-1)
            sys.exit()

print(counts)