n = int(input())
def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)  # n-1개의 원판을 B에 놓고,
        print(a,c)  # 남은 하나의 원판을 A에서 C로 옮긴 후,
        hanoi(n-1,b,a,c)  # B의 원판들을 C에 옮기면 된다.
count = 0
for i in range(n):
    count = 2*count + 1
print(count)
hanoi(n,1,2,3)

# hanoi 함수를 보면 재귀 호출을 할 때 인자의 순서가 다른 것을 볼 수 있는데,
# 원래 인자 순서대로 설명하면 a는 현재 n개의 원판이 쌓여있는 곳,
# b는 n-1개의 원판을 옮겨 놓을 곳,
# c는 a에서 남은 원판을 놓을 곳이 된다.
