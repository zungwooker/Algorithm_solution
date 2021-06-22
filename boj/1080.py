import sys
#cases = sys.stdin.read().splitlines()

N, M = map(int, sys.stdin.readline().rstrip().split())
A, B, C= [], [], [[]]*N

for _ in range(N):
    A.append(sys.stdin.readline().rstrip())
for _ in range(N):
    B.append(sys.stdin.readline().rstrip())
print(C[0])
C.append(1)
print(C)
for i in range(N):
    for j in range(M):
        if A[i][j]!=B[i][j]:
            C[i].append(1)
            print("111", C)
        else:
            C[i].append(0)
            
            print("222", C)
print(C)
"""
for i in range(N-2):
    for j in range(M-2):
        if int(C[i][j])%2==1:
            for x in range(3):
                for y in range(3):
                    C[i+x][j+y] += 1
    for j in range(M):
        if C[i][j]%2==1:
            print(-1)
            sys.exit()
        """