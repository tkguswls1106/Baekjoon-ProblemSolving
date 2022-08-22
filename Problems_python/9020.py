def is_right_sosu(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    else:
        return True

T = int(input())
while (True):
    if(T==0):
        break
    n = int(input())
    a,b = n//2, n//2  # n을 반으로 쪼개고 한 개는 +1씩, 한 개는 -1씩 해보면서 두 수가 모두 소수인지 확인
    while a>0:
        if is_right_sosu(a) and is_right_sosu(b):
            print(a,b)
            break
        else:
            a -= 1
            b += 1
    T-=1