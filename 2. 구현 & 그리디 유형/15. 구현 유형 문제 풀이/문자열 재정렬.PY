S = input()

digitList = []  # 숫자가 들어갈 공백 리스트 생성
stringList = [] # 문자가 들어갈 공백 리스트 생성
testList = ["0","1","2","3","4","5","6","7","8","9"]

for i in range(len(S)): # 입력 받은 문자열 길이에 대하여
    if S[i] in testList:    # i번째 문자가 testList에 있다면
        digitList.append(int(S[i])) # 정수로 추가
    else: stringList.append(S[i])   # 없을 경우는 문자 추가
    
sum = 0
for j in digitList:
    sum += j    # 숫자 리스트의 총합 계산
stringList.sort()   # 문자 리스트 오름차순 정렬

for k in stringList:
    print(k,end='') # 문자 리스트 요소를 하나씩 출력하고 줄을 변경하지 않음
print(sum)