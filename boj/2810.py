N = int(input())
seats = input()
counts = 0

i=0
while i<N:
    if seats[i]=='L':
        counts += 2
        i += 2
        break
    counts += 1
    i += 1

while i<N:
    if seats[i]=='L':
        i += 1
    counts += 1
    i += 1

print(counts)