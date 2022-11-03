arr = []
for i in range (5):
    arr.append(int(input()))

arr.sort()
print(int(sum(arr)/5))
print(arr[int(5/2+1-1)])