import sys

def DateToNumber(f):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(months[:f[0]-1]) + f[1]

N = int(sys.stdin.readline())
fls =[]

for _ in range(N):
    f = list(map(int, sys.stdin.readline().split()))
    if (f[2] > 3 or (f[2] == 3 and f[3] > 1))  and f[0] != 12:
        fls.append([DateToNumber(f[:2]), DateToNumber(f[2:])])

print(fls)