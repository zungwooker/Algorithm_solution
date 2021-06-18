N = int(input())
count = 0

arr = [-1]*1000001
arr[0], arr[1], arr[2], arr[3] = 0, 0, 1, 1

for i in range(2, N+1):
    # 값이 비어있을 때
    if arr[i] == -1:
        arr[i] = arr[i-1] + 1
    # 값이 차있을 때
    else:
        if arr[i] > arr[i-1] + 1:
            arr[i] = arr[i-1] + 1
    ## 값이 들어있는 상태

    if i*2 <= 1000000:
        if arr[i*2]==-1:
            arr[i*2] = arr[i]+1
        else:
            arr[i*2] = min(arr[i]+1, arr[i*2])
    if i*3 <= 1000000:
        if arr[i*3]==-1:
            arr[i*3] = arr[i]+1
        else:
            arr[i*3] = min(arr[i]+1, arr[i*3])
        

print(arr[N])

    
    