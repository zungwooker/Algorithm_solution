n = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort(reverse=True)

for i in range(n):
    A[i] *= B[i]

print(sum(A))