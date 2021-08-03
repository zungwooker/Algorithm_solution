N, L = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()

lastHole = holes[0]
tapes = 1
for i in range(1, N):
    if holes[i] > lastHole+L-1:
        tapes += 1
        lastHole = holes[i]

print(tapes)


