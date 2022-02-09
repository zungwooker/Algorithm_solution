n = int(input())
card = [0] + list(map(int, input().split()))

for i in range(2, n+1):
    for j in range(1, i//2+1):
        if card[i] < card[j] + card[i-j]:
            card[i] = card[j] + card[i-j]

print(card[n])
