# 학생들의 성적을 비교한 결과를 알 때, 정확한 순위를 알 수 있는 학생수 구하기
# 학생들의 성적은 모두 다 다르다.
# 학생의 수 N, 비교한 횟수 M 입력
n, m = map(int, input().split())

# 자신보다 작은 학생 저장할 배열
min_arr = [[] for _ in range(n + 1)]
# 자신보다 큰 학생 저장할 배열
max_arr = [[] for _ in range(n + 1)]
# M개의 성적 비교 결과 입력
for _ in range(m):
    # a번 학생이 b번 학생보다 성적이 낮다는 의미
    a, b = map(int, input().split())
    # a 학생에 대하여 더 잘본 학생 정보 저장
    max_arr[a].append(b)
    # 여기서 b보다 잘 본 학생이 있다면 그 학생은 a보다는 확실히 더 잘본 학생이다.
    max_arr[a].extend(max_arr[b])
    # b 학생에 대하여 더 못본 학생 정보 저장
    min_arr[b].append(a)
    # 여기서 a보다 못 본 학생이 있다면 그 학생은 b보다는 확실히 더 못본 학생이다.
    min_arr[b].extend(min_arr[a])

# 성적 순위를 정확히 알 수 있는 학생 수 출력
# 학생 수 만큼 돌면서 min_arr, max_arr 의 길이의 합이 n - 1이라면 정확한 순위를 알 수 있다.
answer = 0
for i in range(1, n + 1):
    if len(set(min_arr[i])) + len(set(max_arr[i])) == n - 1:
        answer += 1

print(min_arr)
print(max_arr)
# 정답 출력
print(answer)
