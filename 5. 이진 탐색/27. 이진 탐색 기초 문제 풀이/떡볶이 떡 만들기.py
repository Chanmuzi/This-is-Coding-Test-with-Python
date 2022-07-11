import sys

n,m = map(int,sys.stdin.readline().split())
height_list = list(map(int,sys.stdin.readline().split()))

# 최대값을 초기 절단기 높이로 설정
height = max(height_list)
height_sum = 0
# 절단기 높이가 양수일 때
while height > 0:
    for i in height_list:
        # 절단기가 떡보다 더 높으면 계산 x
        if i > height:
            # 떡 높이 - 절단기 높이
            height_sum += (i - height)
    # 잘린 떡 길이 합이 m일 때 중단            
    if height_sum == m: break
    else: # 변수 초기화 및 절단기 높이 감소
        height_sum = 0
        height -= 1

print(height)
