n, k = map(int, input().split())
result = 0

while n>=k:
    result += n%k
    n //= k
    result += 1
    print(n, end='\n')

result += n-1

print(result)