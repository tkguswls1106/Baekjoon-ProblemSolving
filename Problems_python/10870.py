def fibonacci(cnt):
    if cnt==0:
        return 0
    elif cnt==1:
        return 1  # if와 elif 요약하면, if n <= 1: return n
    else:
        return fibonacci(cnt-1)+fibonacci(cnt-2)

n = int(input())
print(fibonacci(n))