import sys
appeared = [False for _ in range(42)]

for i in range(10):
    appeared[int(sys.stdin.readline().rstrip())%42] = True

print(appeared.count(True))
    