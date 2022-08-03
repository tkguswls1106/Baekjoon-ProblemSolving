t = int(input())

result_arr=[]
for m in range(t):
    h, w, n = map(int, input().split())
    arr = []
    for j in range (1,w+1):
        for k in range(1,h+1):
            arr.append(str(k)+str(j).zfill(2))
    result_arr.append(arr[n-1])

for i in range(t):
    print(result_arr[i])

# h를 가로로, w를 세로로하여 구한방법이다.