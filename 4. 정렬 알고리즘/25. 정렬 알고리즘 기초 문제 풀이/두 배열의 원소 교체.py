n,k = map(int,input().split())

# 리스트 a와 b를 입력받은 숫자들로 구성
array_a = list(map(int,input().split()))
array_b = list(map(int,input().split()))

# 바꿔치기는 최대 n번까지 가능하므로 최댓값 미리 구하기
original_max = 0
for i in array_b:
    original_max += i

for i in range(k):
    # 최소 인덱스 초기화
    min_index_a = 0
    # 최소 값 초기화
    min_value_a = 0

    min_value_a = min(array_a)
    min_index_a = array_a.index(min_value_a)

    # 최대 인덱스 초기화
    max_index_b = 0
    # 최대 값 초기화
    max_value_b = 0
    
    max_value_b = max(array_b)
    max_index_b = array_b.index(max_value_b)

    # 배열 A 최소값과 배열 B 최대값 swap
    array_a[min_index_a], array_b[max_index_b] = array_b[max_index_b], array_a[min_index_a]

# 배열 A 모든 원소 합 출력
result = 0
for i in array_a:
    result += i

print(result)