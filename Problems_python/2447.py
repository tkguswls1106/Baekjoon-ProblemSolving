def star(n):
    if n==3:
        return ['***','* *','***']
        
    arr = star(n//3)
    star_arr = []

    for i in arr:
        star_arr.append(i*3)

    for i in arr:
        star_arr.append(i + ' '*(n//3) + i)

    for i in arr:
        star_arr.append(i*3)

    return star_arr

n = int(input())
print('\n'.join(star(n)))  # join은 리스트를 문자열로 이어붙여서 저장할때 사용

# arr = ['가나다','라마바','사아자']
# a = []
# for i in arr:
#     a.append(i*2)
# print(a)
# # 출력이 ['가나다가나다', '라마바라마바', '사아자사아자'] 이렇게 뜬다.