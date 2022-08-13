n = int(input())
numbers_arr = list(map(int, input().split()))

count = 0

# 소수는 1과 본인 숫자가 약수인 숫자이다.
for i in numbers_arr :
  check = 0
  if i == 1 :  # i가 1이라면, 소수가 아니므로 제외.
    continue
  for j in range(2, i) :  # i를 2~i-1 숫자로 나누었을때 check=1이상이라면 소수가 아님.
                          # 왜냐하면 본인 숫자인 i와 1 외에 또다른 나뉘는 숫자가 존재하기때문이다.
    if i % j == 0 :
      check = 1
  
  if check == 0 :
    count += 1

print(count)