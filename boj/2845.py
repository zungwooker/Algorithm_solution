from hashlib import new


L, P = map(int, input().split())
fact = L*P
news = list(map(int, input().split()))
for x in news:
    print(x-fact, end=' ')