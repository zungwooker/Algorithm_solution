import sys

def noMarchNovember(A, Z):
    if A[0] > 3:
        return True
    elif A[0] == 3 and A[1] > 1:
        return True
    if Z[2] < 12:
        return True
    return False

def beforeMarch1(A):
    if A[2] < 3:
        return True
    else:
        return False

def bloomBeforeMarch2(A):
    if A[0]<3:
        return True
    elif A[0]==3 and A[1] == 1:
        return True
    else:
        return False

def overNovember30(Z):
    if Z[2] == 12 and Z[3] >= 1:
        return True
    else:
        return False

def AthanZ(A, Z):
    if A[2] < Z[2]:
        return True
    elif A[2] == Z[2] and A[3] < Z[3]:
        return True
    else:
        return False

def emptyDay(end, start):
    if end[2] < start[0]:
        return True
    elif end[2] == start[0] and end[3] < start[1]:
        return True
    else:
        return False

def needPop(selected, flowers, idx):
    if (len(selected) > 1 and not emptyDay(selected[-2], flowers[idx])) or (len(selected) == 1 and bloomBeforeMarch2(flowers[idx]) and AthanZ(selected[-1], flowers[idx])):
        return True
    else:
        return False

N = int(sys.stdin.readline())
fls = []
sld = []
for i in range(N):
    fls.append(list(map(int, sys.stdin.readline().split())))

fls.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]))

# 시작이 3월 1일보다 느리거나, 12월 1일보다 일찍 진다면 0 출력과 끝
if noMarchNovember(fls[0], fls[-1]):
    print(0)
    exit()

i = 0 # 시작하는 꽃의 idx
j = N-1 # 끝나는 꽃의 idx
while beforeMarch1(fls[i]):
    i += 1
while overNovember30(fls[j]):
    j -= 1

if i != 0:
    i -= 1
if j != N-1:
    j += 1

sld.append(fls[i])
i += 1
while i < j+1:
    if emptyDay(sld[-1], fls[i]): # 꽃이 없는 날이 존재
        print(0)
        exit()
    if AthanZ(sld[-1], fls[i]): # 꽃이 존재하며 다음 꽃이 선택한 마지막 꽃보다 늦게 질 때
        if needPop(sld, fls, i):
            sld.pop()
        sld.append(fls[i])
    i += 1

print(len(sld))

