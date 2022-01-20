import itertools

N, K = int(input()), int(input())
cards = [input().rstrip() for _ in range(N)]
pairs = set(map(''.join, itertools.permutations(cards, K)))
print(len(pairs))