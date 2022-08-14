m = int(input())
n = int(input())

sosu_arr = []
for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2, i):  # for~else 구문 사용
        if i%j==0:
            break
    else:
        sosu_arr.append(i)

if len(sosu_arr)==0:
    print(-1)
else:
    print(sum(sosu_arr))
    print(min(sosu_arr))