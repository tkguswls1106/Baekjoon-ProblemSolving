def factorial(num):
    if num==0:
        return 1  # 0팩토리얼은 1이다.
    else:
        return num * factorial(num - 1)

n = int(input())
print(factorial(n))