# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
data = []
for _ in range(n):
    name, score = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    data.append((name, int(score)))

data.sort(key=lambda x: x[1])

# 정렬이 수행된 결과를 출력
for student in data:
    print(student[0], end=' ')
