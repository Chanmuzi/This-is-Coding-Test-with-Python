n,m = map(int,input().split())

my_list = []

for i in range(n):
    s = input()
    my_list.append([])
    for j in s:
        my_list[i].append(int(j))

print(my_list)

for i in range(n):
    for j in range(m):
        if my_list[i][j] == 0:
            my_list[i][j] = 1

# 리스트만 생성하고 포기
# 재귀함수로 풀어야한다는 생각을 못했음            