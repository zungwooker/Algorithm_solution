import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
sch = list(map(int, sys.stdin.readline().rstrip().split()))

app = [[] for _ in range(K+1)] # app[i] == i가 사용된 시간
for i in range(len(sch)):
    app[sch[i]].append(i)

t = 0
taps = []
while len(taps)<N:
    if not sch[t] in taps:
        taps.append(sch[t])
    del app[sch[t]][0]
    t += 1

counts = 0
while t<K:
    if not sch[t] in taps:
        far = 0
        farIndex = 0
        for i in range(len(taps)):
            if len(app[taps[i]]) == 0:
                farIndex = i
                break
            if app[taps[i]][0] > far:
                far = app[taps[i]][0]
                farIndex = i
        taps[farIndex] = sch[t]
        counts += 1
    del app[sch[t]][0]
    t += 1

print(counts)


        