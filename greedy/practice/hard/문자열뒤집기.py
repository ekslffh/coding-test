s = input()

array = [0] * 2

value = int(s[0])
array[value] += 1

for i in range(1, len(s)):
    if value != int(s[i]):
        value = int(s[i])
        array[value] += 1

print(min(array))
