for _ in range(20):
    a = input().split()
    print("(", end='')
    for i in range(len(a)-1):
        print("'", end='')
        print(a[i], end='')
        print("', ", end='')
    print("'", end='')
    print(a[-1], end='')
    print("'", end='')
    print("),")