# [백준온라인저지 알고리즘 파이썬 정리 노트 / ps(problem solving) 필기]

**백준 단계별로 풀어보기 사이트: https://www.acmicpc.net/step**
```
출력할때, 따옴표 안에 따옴표 출력할때는 주로 ""큰따옴표 안에 ''작은따옴표를 넣는다.
print(" 'hello world' ")
여기서 추가적인 내용은, 만약에 큰따옴표 안에 큰따옴표를 출력할경우에는, 해당 큰따옴표" 앞에 \를 붙여준다.
print(" \"hello world\" ")

출력할때, 안에 역슬래쉬를 출력하고싶을때는, 역슬래쉬 앞에 \를 붙여서 출력한다.
print("\\")

max( )  // 괄호 안에 인자로 넣은 매개변수들끼리 비교해서 가장 큰 값 반환함.
          // 괄호안에 리스트 이름 넣어서 리스트 요소중 가장 큰값도 반환이 가능함.
min( )  // 괄호 안에 인자로 넣은 매개변수들끼리 비교해서 가장 작은 값 반환함.
          // 괄호안에 리스트 이름 넣어서 리스트 요소중 가장 작은값도 반환이 가능함.
sum()  // 괄호안에 리스트 이름 넣어서 리스트 요소들을 모두 더한값도 반환이 가능함.
여기서 주의할점은, sum(), min(), max() 같은 예약어를 변수명으로 다시 사용할 경우 에러가 난다. 예를들어 sum=sum(arr) 같은 경우이다.

arr.index(num)  // num값이 들어있는 arr리스트의 인덱스값을 반환한다.

for i in range (5)  // i는 0~4 까지 반복된다.
for i in range(0, 10, 2)  // 이건 0부터 10전까지(9까지) 2씩 증가한 숫자중에서 반복한다. 즉 0부터 짝수만.
for i in range(10, 0, -1)  // 10에서 0후까지(1까지) 역순으로 -1씩 해가며 반복한다.

arr = list(map(자료형, 리스트)) 이기때문에,
리스트 자리에 input().split()으로 생성한 리스트가 들어갈수도, for문으로 str(i)하여 만든 리스트가 들어갈수도 있는것이다.

<공백구분 리스트값 입력하기>
for반복문 안에 n = list(map(int, input().split())) 이런것처럼 리스트를 map으로 input()으로 입력받는걸 생성하지 못한다.
그러니까 그냥 n = list(map(int, input().split())) 이렇게 단독으로 사용하자.

<엔터구분 리스트값 입력하기>
arr = []
for i in range(n):
    arr.append(int(input()))

while 무한반복문에서, 수가 입력되지 않아서 에러가 발생하면 반복문을 끝낼 수 있도록 하려면
try - except 구문을 활용하면 된다.
예를들어
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b) 

a = str(num)  // int형 num숫자를 문자열 형태로 변환함.
arr = list(문자열)  // 문자열을 리스트로 변환함.

arr.count(num)  // 리스트에서 특정 값인 num의 개수를 구함
arr.remove(num)  // 리스트에서 num값을 삭제함.

arr = [i for i in range(10)]  // 0부터 9까지 숫자를 생성하여 리스트 생성
a = list(range(3, 10))  // a를 출력하면 [3, 4, 5, 6, 7, 8, 9]

세트 사용
arr = set('apple')
arr  #{'e', 'l', 'a', 'p'}

set 끼리의 - 는 가능하기때문에,
보통 삭제연산을 많이사용할때는 리스트의 remove를 사용하기보단
세트끼리 뺄셈을 하여 결과값을 구하는 방식을 사용한다.

리스트.sort()와 sorted(리스트)의 가장 큰 차이는
리스트.sort() 는 본체의 리스트를 정렬해서 변환하는 것이고,
sorted(리스트) 는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것이다.

문자열로 이루어진 리스트가 있고, 각 리스트의 각 인덱스의 문자열에서 문자만 활용하고싶다면,
가장 바깥쪽 for문에 input문장을 넣고, for문을 하나 더 중첩시키자.
예를들어
for i in range(n):
     arr = list(input())
     for ch in arr:
          if ch=='O':
               print("Y")
          else:
               print("N")

파이썬 함수 만드는법: https://blockdmask.tistory.com/440
파이썬 함수 전역변수 지역변수 다루는법: http://www.tcpschool.com/python2018/python_function_scope

정수형을 유니코드 문자형으로 바꿀때 chr 사용.
n = int(input())
print(chr(n))  // n에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 
예를들어 n에 65를 입력하면, 출력은 A가 된다.

문자형을 유니코드 정수형으로 바꿀때 ord 사용.
c = ord(input())
print(c)
예를들어 c에 A를 입력하면, 출력은 65가 된다.

딕셔너리이름.setdefault(키, 값)  // 해당 딕셔너리에 키와 값을 새로 추가한다.

파이썬 라이브러리로 알파벳이나 숫자 목록이 담긴 리스트를 만들 수 있다.
import string 
// string.ascii_lowercase 는, 소문자 abcdefghijklmnopqrstuvwxyz
// string.ascii_uppercase 는, 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
// string.ascii_letters 는, 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
// string.digits 는, 숫자 0123456789
쓰임예시로는
lo_arr = list(string.ascii_lowercase)
up_arr = list(string.ascii_uppercase)
al_arr = list(string.ascii_letters)
nu_arr = list(string.digits)
print(lo_arr)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = list(range(97, 123))  // 아스키코드 문자 a~z 까지를 십진수로 나타내면 97~122 이다. 나중에 chr()로 변환해서 응용하면 된다.
alphabet = list(range(65, 91))  // 아스키코드 문자 A~Z 까지를 십진수로 나타내면 65~90 이다. 나중에 chr()로 변환해서 응용하면 된다.

문자열 = 문자열.lower()  // 문자열 소문자로 변환
문자열 = 문자열.upper()  // 문자열 대문자로 변환

문자열 뒤집기
str = input().split()  // 123 입력 (문자열)
str = a[::-1]  // str = 321 (문자열)
str = int(str)  // str = 321 (정수형)

a = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in range (len(a)):
        for j in dial:
                if a[i] in j:  # a[i]==j 라고하면 틀리다.
                        print(dial.index(j))  # j가 들어있는 dial의 인덱스값

{ 백준 내코드에 반례가 있어(예를들어 aabcbb) 완벽한 코드는 아니지만, 중첩 for문과 if문 속에서 break와 continue의 사용법을 보기에 좋은 예시 }
# 백준 파이썬 1316번
n = int(input())
cnt = 0
result_cnt = 0
for i in range (n):
        a = input()
        for j in range (len(a)):
                        if a.count(a[j]) > 1:  # 중복된것이 있음
                                if a.index(a[j])+1 < a.find(a[j],(a.index(a[j])+1)):  # 중복된것이 연속되지않음
                                        break  # 안쪽 for문을 끝내고 바깥쪽 for문으로 이동함.
                                               # 만약 break가 아니라 continue를 적었다면,
                                               # 안쪽 for문을 마저 이어서하여 문자열 a의 다음 문자도 비교했을것이다.
                                               # 어차피 한 문자라도 삑사리나면 그건 result_cnt = 0 으로 치고 다음 새롭게 입력받은 문자열로 넘어가야하는데
                                               # continue를 써버리면 예를들어 abba 입력시 ab보고 끝냈을것을 남은 ba도 확인하게되어 result_cnt값에 여지를 주게 되는 것이다.
                                else:  # 중복된 값이 연속된것임
                                        cnt+=1
                        else:  # 중복된것이 없음
                                cnt+=1
        if cnt>=1:
                result_cnt+=1
        cnt=0       
print(result_cnt)

리스트 마지막 인덱스의 요소를 출력하고 싶다면,
print(arr[-1]) 이런식으로 -1 인덱스로 적어주면 된다.

------------ 2차원 리스트 관련 ------------

-- 출력 방법 --

<for문 한 번 쓰기>
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:
    print(x, y)
# 10 20
# 30 40
# 50 60

<for문 두 번 쓰기>
a = [[10, 20], [30, 40], [50, 60]]

for i in a:        # a에서 안쪽 리스트를 꺼냄
    for j in i:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()
# 10 20
# 30 40
# 50 60

<range 사용하기>
a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)):            # 세로 크기
    for j in range(len(a[i])):     # 가로 크기 a[i] [값, 값]의 len은 2
        print(a[i][j], end=' ')
    print()
# 10 20
# 30 40
# 50 60

-------------

-- 생성 방법 --

<비어있는 2차원 리스트 생성방법>  // [[0,0],[0,0],[0,0]]
a = []
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)
print(a)

< 리스트 표현식으로 2차원 리스트 만들기>  // [[0,0],[0,0],[0,0]]
a = [[0 for j in range(2)] for i in range(3)]

<위 방식을 응용한 또다른 방법>  // [[0,0,0,], [0], [0,0,0], [0,0], [0,0,0,0,0]]
a = [[0]* i for i in [3, 1, 3, 2, 5]]

-------------

---------------------------------------

< 소수 판별 알고리즘 '에라토스테네스의 체' >
# 백준 파이썬 1929번 문제
# m이상 n이하의 숫자중 소수를 판별하여 출력하는 문제
m,n = map(int, input().split())
for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2, int(i**0.5)+1):  # range(2, i) 으로 적으면 시간 초과 실패가 뜬다.
                                       # 제곱근 값으로 범위 설정해주자.
                                       # '에라토스테네스의 체'라는 소수 판별 알고리즘이다.
                                       # 이는 특정한 숫자의 제곱근까지만 약수의 여부를 검증하는 방식으로써, 실행 시간이 단축된다.
                                       # 약수는 대칭으로 이루어져있기 때문에, 예를들어 12의 약수는 1 2 3 4 6 12 / 1*12 , 2*6, 3*4 로 대칭인것이다.
                                       # int(i**0.5)+1 에서 +1의 이유는, 만약 제곱근이 아닌 일반적인 방법이었다면, 2~i-1 값까지만 나눠보면 되어 range(2, i)로 for문을 돌리면 되지만,
                                       # 제곱근 방법은 2~제곱근값 까지 모두 for문으로 돌려 나눠보아야하기때문에 range 범위 마지막에 +1을 해준것이다.
        if i%j==0:
            break
    else:
        print(i)

for i in range (2,2) 처럼 범위가 이러한 경우일때는, 2~1 범위라서
해당 for문 안의 코드가 실행되지 않는다.
하지만 만약 저러한 for문의 범위에 for~else 구문을 사용할 경우에는 else 부분의 코드만 실행된다.

브루트 포스(brute force)란,
완전탐색 알고리즘이다. 즉, 가능한 모든 경우의 수를 모두 탐색하면서 요구조건에 충족되는 결과만을 가져온다.

sys.stdin.readline() 가 input() 보다 빠른 입력방법이다.
그리고 sys.stdin.readline() 를 사용하려면 import sys 써야한다.
input()과 sys.stdin.readline()의 차이점 설명: https://buyandpray.tistory.com/7

Counter과 most_common 에 대하여: https://www.daleseo.com/python-collections-counter/

---------------------------------------

< 정렬 방법 >

리스트에서 단어의 길이 순으로 오름차순 정렬 방법은,
리스트명.sort(key=len)

a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

# 인자없이 그냥 sorted()만 쓰면, 리스트 아이템의 각 요소 순서대로 정렬을 한다.
b = sorted(a)
# b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
c = sorted(a, key = lambda x : x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]  // (이거, ?) 기준 정렬
d = sorted(a, key = lambda x : x[1])
# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]  // (?, 이거) 기준 정렬

# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
f = sorted(e, key = lambda x : (x[0], -x[1]))
# f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]

< 정렬 예시 >

# 문제는 백준 1181.py

N=int(input())
arr_set = set()
for i in range(N):
    arr_set.add(input())
arr = list(arr_set)
arr.sort()  # arr.sort(key=len) 이거한 다음에
arr.sort(key=len)  # arr.sort() 이거하는건 안됨.
for i in range(len(arr)):
    print(arr[i])

# 이거도 가능
# N=int(input())
# arr_set = set()
# for i in range(N):
#     arr_set.add(input())
# arr = list(arr_set)
# arr2 = sorted(arr)  # arr2 = sorted(arr, key=len) 이거한 다음에
# arr3 = sorted(arr2, key=len)  # arr3 = sorted(arr2) 이거하는건 안됨.
# for i in range(len(arr3)):
#     print(arr3[i])

---------------------------------------

```