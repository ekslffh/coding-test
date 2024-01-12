# 학생 수 입력받기
n = int(input())

# 학생 수만큼 이름, 성적 입력받기
array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

sorted_array = sorted(array, key=lambda x: x[1])

for i in sorted_array:
    print(i[0], end=' ')
