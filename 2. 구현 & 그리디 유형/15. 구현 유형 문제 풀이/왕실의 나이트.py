# 입력받을 문자를 숫자로 바꾸기 위해 딕셔너리를 생성한다
columnDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}  
a = input()
myKey = a[0]    # 문자열의 첫 번째 문자를 딕셔너리의 key로 사용한다
myColumn = columnDict[myKey]

dx = [2,2,-2,-2,1,1,-1,-1]  # 말이 이동할 수 있는 8가지의 경우
dy = [1,-1,1,-1,2,-2,2,-2]

x = int(a[1])   # 입력받은 문자열의 두 번째 문자를 정수형으로 변환
y = myColumn
nx = x  # 나이트의 초기 위치 설정
ny = y
count = 0   # 이동 가능한 횟수

for i in range(8):  # 이동해 볼 수 있는 8가지의 케이스에 대하여
    nx += dx[i]     # 실제 이동을 수행해본다
    ny += dy[i]
    if 1 <= nx <= 8 and 1<= ny <= 8:    # 체스판을 벗어나지 않으면
        count += 1
        nx = x  # 위치 초기화
        ny = y
    else:
        nx = x  # 위치 초기화
        ny = y
        continue # 위치만 초기화하고 다음 i에 대한 연산 수행

print(count)