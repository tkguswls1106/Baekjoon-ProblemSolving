n = int(input())
insu = n-1
insu_arr=[]

while (insu!=1 and insu!=0):
    if n%insu==0:
        insu_arr.append(n//insu)
        n=insu
    insu-=1
else:
    if len(insu_arr)==0:
        if n==1:
            print()
        else:
            print(n)
    elif len(insu_arr)!=0:
        insu_arr.append(n)
        for i in range(len(insu_arr)):
            print(sorted(insu_arr)[i])  # 어차피 append하면서 오름차순으로 넣어서, sort 안해도 상관없었음.