T = int(input())

for i in range(T):
    h, w, n = map(int, input().split( )) # h=각 호텔의 층 수, w=각 층의 방 수, n=몇 

    floor = n % h 
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    
    print(floor * 100 + room_line)

# 손님의 번호가 H를 넘어가게 된다면 N % H(N번째 손님을 층수로 나눈 나머지)만큼의 층에 머무르고
# (N//H) + 1만큼 엘리베이터에서 떨어진곳에 머무르는 것이다. 이때 나머지가 0으로 나눠 떨어질때를 고려해야한다.