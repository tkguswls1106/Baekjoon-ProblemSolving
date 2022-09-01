# 입력값(분해합 값) = N
# 반대로, 생성자를 구하려면 분해합을 구하는 과정 중 N은 놔두고
# N의 각 자릿수의 합만 빼주면 된다.

N = int(input())
min_N = abs(N - (len(str(N)) * 9))

for i in range(N):
    temp = sum(map(int, str(i)))  # 문자열의 각 자리를 int로 바꾸어 sum값을 구함. 그리고 temp에 할당함.
    result = i + temp
    if result == N:  # 만약 result==분해합 이면, i는 생성자이다.
        print(i)
        break
else:  # for문에서 break가 한번도 실행되지 않았을 경우
    print(0)