N=int(input())
arr=[]
for i in range(N):
    a, b = map(int,input().split())
    arr.append([b, a])
arr.sort()
for i in range(N):
    print(arr[i][1], arr[i][0])