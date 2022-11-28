N=int(input())
arr_set = set()
for i in range(N):
    arr_set.add(input())
arr = list(arr_set)
arr.sort()  # arr.sort(key=len) 이거한 다음에
arr.sort(key=len)  # arr.sort() 이거하는건 안됨.
for i in range(len(arr)):
    print(arr[i])

# 이거도 가능
# N=int(input())
# arr_set = set()
# for i in range(N):
#     arr_set.add(input())
# arr = list(arr_set)
# arr2 = sorted(arr)  # arr2 = sorted(arr, key=len) 이거한 다음에
# arr3 = sorted(arr2, key=len)  # arr3 = sorted(arr2) 이거하는건 안됨.
# for i in range(len(arr3)):
#     print(arr3[i])