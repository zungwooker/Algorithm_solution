import sys

def DateToNumber(f):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(months[:f[0]-1]) + f[1]

N = int(sys.stdin.readline())
fls =[]
sld = []
result = 0
start = DateToNumber([3,1])
end = DateToNumber([12,1])

for _ in range(N):
    f = list(map(int, sys.stdin.readline().split()))
    if (f[2] > 3 or (f[2] == 3 and f[3] > 1))  and f[0] != 12:
        bloom = DateToNumber(f[:2])
        fall = DateToNumber(f[2:])
        if bloom < start:
            bloom = start
        if fall > end:
            fall = end
        fls.append([bloom, fall])

fls.sort()

sld.append(fls[0])

for f in fls[1:]:
    if sld[-1][1] < f[1]:
        if sld[-1][1] < f[0]:
            print(0)
            exit()
        elif sld[-1][1] == f[0]:
            sld.append(f)
        elif sld[-1][1] > f[0]:
            if (sld[-1][0] == f[0]) or (len(sld) > 1 and sld[-2][1] >= f[0]):
                sld.pop()
            sld.append(f)

if sld[-1][1] < end or sld[0][0] > start:
    print(0)
    exit()

print(len(sld))