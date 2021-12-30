N = int(input())
K = int(input())
noCenterDistance = 0
maxDistance = 0
sensors = list(map(int, input().split()))
sensors.sort()

maxDistance = sensors[-1] - sensors[0]

intervalOfSensors = []
for i in range(1, N):
    intervalOfSensors.append(sensors[i] - sensors[i-1])

intervalOfSensors.sort()

if N-1>K-1:
    for _ in range(K-1):
        noCenterDistance += intervalOfSensors.pop(-1)
else:
    for _ in range(N-1):
        noCenterDistance += intervalOfSensors.pop(-1)

print(maxDistance-noCenterDistance)