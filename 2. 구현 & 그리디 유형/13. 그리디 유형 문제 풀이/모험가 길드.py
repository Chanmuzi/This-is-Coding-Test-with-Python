n = int(input())
a = list(map(int,input().split()))
a.sort()
GroupCount = 0
i = 0

while i < len(a):
    if a[i] == max(a[i:(a[i]+i)]):
        GroupCount += 1
        i += a[i]
    else: i += 1
print(GroupCount-1)