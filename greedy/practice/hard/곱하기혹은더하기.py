s = input()

result = 0
for i in range(len(s)):
    if result == 0 or int(s[i]) == 0:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)
