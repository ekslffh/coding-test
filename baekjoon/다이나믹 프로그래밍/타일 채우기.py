# 타일 채우기

size = 30
arr = [0] * (size + 1)
arr[0] = 1
arr[2] = 3

for x in range(4, size + 1, 2):
    arr[x] = arr[x - 2] * 3 + arr[x - 4] * 2

n = int(input())

print(arr[n])
print(arr)
