import sys
input = sys.stdin.readline

answer = []
# 테스트 케이스 만큼 반복
for _ in range(int(input())):
    # 지원자 수 입력
    n = int(input())
    # 지원자 수 만큼 돌면서 1,2차 성적 입력
    applicants = []
    for _ in range(n):
        applicants.append(tuple(map(int, input().split())))
    # 지원자들 1, 2차 순으로 오름차순 정렬 수행
    applicants.sort()
    # 각 지원자 별로 돌면서 검사하기
    cnt = 1
    compare = applicants[0][1]
    for i in range(1, n):
        # 내가 2차 점수가 더 좋다면, 통과이고 compare를 내 순위로 갱신
        if compare > applicants[i][1]:
            cnt += 1
            compare = applicants[i][1]

    answer.append(cnt)

for x in answer:
    print(x)
