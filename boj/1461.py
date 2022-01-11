N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()
result = 0
i = 0
while i < N and books[i] <= 0:
    i += 1

frontBooks = i
backBooks = N-i
frontIdx = 0
backIdx = -1

while frontBooks:
    result += -books[frontIdx] * 2
    if frontBooks >= M:
        frontBooks -= M
        frontIdx += M
    else:
        frontBooks = 0

while backBooks:
    result += books[backIdx] * 2
    if backBooks >= M:
        backBooks -= M
        backIdx -= M
    else:
        backBooks = 0

result -= max(-books[0], books[-1])
print(result)