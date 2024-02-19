# 국어순, 영어순, 수학순, 이름순서대로 정렬하기

# 학생 수 입력받기
n = int(input())

# n명의 학생에 대한 이름, 국어, 영어, 수학 점수 순서대로 입력받기
data = []
for _ in range(n):
    name, kor, eng, math = input().split()
    data.append((int(kor), int(eng), int(math), name))

data.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for x in data:
    print(x[3])
