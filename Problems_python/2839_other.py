num = int(input())
count = 0

while num >= 0:
    if num % 5 == 0:
        count += int(num // 5)
        print(count)
        break
    else:
        num -= 3
        count += 1
else:
  print(-1)

# while ~ else 문을 사용하였다.