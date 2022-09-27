import sys

N = int(input())

arr = []
for i in range (N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

for element in arr:
    print(element)