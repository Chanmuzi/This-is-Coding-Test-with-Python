a = input()
result = 0

for i in range(len(a)):
      if (result + int(a[i])) >= (result * int(a[i])):
            result += int(a[i])
      else: result *= int(a[i])

print(result)