m,n = map(int, input().split())

for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2, int(i**0.5)+1):  # range(2, i) 으로 적으면 시간 초과 실패가 뜬다.
                                       # 제곱근 값으로 범위 설정해주자.
                                       # '에라토스테네스의 체'라는 소수 판별 알고리즘이다.
                                       # 이는 특정한 숫자의 제곱근까지만 약수의 여부를 검증하는 방식으로써, 실행 시간이 단축된다.
        if i%j==0:
            break
    else:
        print(i)