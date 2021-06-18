S = int(input())
idx = 1
count = 0
while S>0:
    S -= idx
    count += 1
    idx += 1

if S==0:
    print(count)
else:
    print(count-1)