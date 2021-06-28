import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    change = int(sys.stdin.readline().rstrip())
    print(change//25, end=' ')
    change = change%25
    print(change//10, end=' ')
    change = change%10
    print(change//5, end=' ')
    change = change%5
    print(change)