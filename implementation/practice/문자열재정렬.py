word = input()

hap = 0
arr = []

for i in word:
    if i.isdigit():
        hap += int(i)
    elif i.isalpha():
        arr.append(i)

arr.sort()
arr.append(hap)

for a in arr:
    print(a, end='')
