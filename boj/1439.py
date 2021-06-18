S = str(input())

semaphore = False
counts = 0

for i in S:
    if i != S[0] and semaphore == False:
        semaphore = True
        counts += 1
    if i == S[0]:
        semaphore = False

print(counts)
