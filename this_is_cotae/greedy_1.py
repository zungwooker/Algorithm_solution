N, M, K = map(int, input().split())
arr = input().split()

for i in range(N):
    arr[i] = int(arr[i])
arr.sort(reverse=True)

print( int((M/(K+1))*(K*arr[0]+arr[1]) + (M%(K+1)*arr[0])) )
