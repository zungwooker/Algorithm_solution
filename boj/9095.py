t = int(input())
methods = [0]*11
methods[0] = 1
methods[1] = methods[0] + 1
methods[2] = methods[1] + methods[0]+ 1
for i in range(3, 11):
    methods[i] = methods[i-1] + methods[i-2] + methods[i-3]

while t:
    print(methods[int(input())-1])
    t -= 1