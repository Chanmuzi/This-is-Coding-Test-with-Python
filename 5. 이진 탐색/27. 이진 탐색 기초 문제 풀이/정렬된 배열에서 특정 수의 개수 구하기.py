from bisect import bisect_left, bisect_right
import sys

n,x = map(int,sys.stdin.readline().split())
num_list = sorted(list(map(int,sys.stdin.readline().split())))

# 기존 리스트 내 원소 x 바로 왼쪽과 오른쪽 위치
min_x = bisect_left(num_list, x)
max_x = bisect_right(num_list, x)

# 리스트에 x인 원소가 존재하지 않는다면
if min_x == n:
    print(-1)
# 리스트에 x인 원소가 존재한다면    
else: print(max_x - min_x)
