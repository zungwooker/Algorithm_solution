N, K = input().split()
emts = list(input().split())
emts.sort(reverse=True)
res = []

for i in range(len(N)):
    for j in range(int(K)):
        if emts[j] == N[i]:
            res.append(emts[j])
            break

        if emts[j] < N[i]:
            res.append(emts[j])
            for _ in range(len(N)-i-1):
                res.append(emts[0])
            break

        if j == int(K)-1:
            res.pop()
            for k in range(1, int(K)):
                if emts[j] < N[i-1]:
                    res.append(emts[j])
                    break
            for _ in range(len(N)-i):
                res.append(emts[0])
            break

    if len(res) == len(N):
        break

for num in res:
    print(num, end='')