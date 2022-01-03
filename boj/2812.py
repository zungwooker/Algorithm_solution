N, K = map(int, input().split())
a = list(input())
result = []
result.append(a[0])

for num in a[1:]:
    while K > 0 and len(result) > 0 and result[-1] < num:
        result.pop()
        K -= 1
    result.append(num)

print("".join(result[:len(result)-K]))
