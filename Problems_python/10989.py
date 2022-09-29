import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):  # 동일한 숫자 여러번 출력하도록 고려한 코드부분
            print(i)

# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못한다.
# 그래서 입력값이 10000개 까지 주어질 수 있으니 10000개 만큼의 리스트를 만들어 놓는다.
# 그러나 인덱스는 0부터 세기 때문에 이를 계산하기 편하게 길이가 10001인 리스트를 만든다.
# 리스트에 각 요소마다 0을 할당해놓고 입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1씩 해준다.
# 나중에 입력을 다 받고나면 0보다 큰 요소를 갖는 인덱스들을 찾아서 그 수만큼 인덱스를 출력해주면 된다.