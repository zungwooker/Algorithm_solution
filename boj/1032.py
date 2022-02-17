N = int(input())
files = [input() for _ in range(N)]
result = ''

for i in range(len(files[0])):
    for j in range(1, N):
        if files[0][i] != files[j][i]:
            result += '?'
            break
    if i == len(result):
        result += files[0][i]

print(result)