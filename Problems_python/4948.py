# < 주어진 제한 1 ≤ n ≤ 123,456 을 이용한 정상시간 버전 >
sosu_arr = []
for i in range(2, 246913):  # 2n보다 같거나 작은소수이므로, 123456*2+1 범위로 range를 설정한다.
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            break
    else:
        sosu_arr.append(i)

while(True):
    count = 0
    n = int(input())
    if n==0:
        break
    for sosu in sosu_arr:
        if n<sosu<=2*n:
            count+=1
    print(count)


# # < 시간초과 버전 >
# while(True):
#     count = 0
#     n = int(input())
#     if n==0:
#         break
#     for i in range(n+1, n*2+1):
#         for j in range(2, int(i**0.5)+1):  # '에라토스테네스의 체' 제곱근 소수 판별 알고리즘
#             if i%j==0:
#                 break
#         else:
#             count+=1
#     print(count)