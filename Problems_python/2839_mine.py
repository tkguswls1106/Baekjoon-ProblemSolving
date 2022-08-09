n = int(input())

five = n//5
three = n//3
arr = []

for i in range(0, three+1):
    for j in range(0, five+1):
        if i*3+j*5==n:
            arr.append(i+j)

if len(arr)==0:
    print(-1)
else:
    print(sorted(arr)[0])