i = 1
while True:
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    print("Case ", i, ": ", (V//P)*L+min(V%P, L), sep='')
    i += 1