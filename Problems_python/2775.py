t = int(input())

for i in range (t):
    k = int(input())
    n = int(input())

    arr_k = list(range(1,n+1))
    arr = []
    arr.append(arr_k)

    for j in range (k):
        for idx in range(1,len(arr_k)):
            arr_k[idx] = arr_k[idx-1]+arr_k[idx]
        arr.append(arr_k)

    print(arr[k][n-1])