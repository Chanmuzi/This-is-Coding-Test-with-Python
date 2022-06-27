n = int(input())
plan = list(input().split())

x = 0
y = 0

for i in range(len(plan)):
    if plan[i] == 'L':
        if y == 0:
            continue
        else:
            y -= 1
    elif plan[i] == 'R':
        if y == n-1:
            continue
        else:
            y += 1
    elif plan[i] == 'U':
        if x == 0:
            continue
        else:
            x -= 1
    elif plan[i] == 'D':
        if x == n-1:
            continue
        else:
            x += 1

print((x+1),(y+1))