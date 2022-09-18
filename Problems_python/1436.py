# 666이라는 숫자가 들어가는 숫자의 오름차순 순서이다.

N = int(input())

cnt = 0
num_int = 665
while(N != cnt):
    if('666' in str(num_int)):
        cnt+=1
    if N != cnt:
        num_int+=1

print(num_int)

# # 이 방법도 가능
# N = int(input())

# arr = []
# num_int = 665
# while(len(arr)!=10000):
#     if('666' in str(num_int)):
#         arr.append(num_int)
#     num_int+=1

# print(arr[N-1])