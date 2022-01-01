N = int(input())
dis = list(map(int, input().split()))

dis.remove(max(dis))
print(sum(dis))