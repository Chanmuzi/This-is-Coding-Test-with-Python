N = int(input())
count = 0
result = 0

for i in range(1,61):
    if (i%10) == 3 or (30<=i<40):
        count += 1
count = 15*60 + 45*15

for j in range(N+1):
    if j == 3 or j == 13:
        result += 3600
    else: result += count
    
print(result)