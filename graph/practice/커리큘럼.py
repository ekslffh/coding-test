# N개의 강의를 듣고자 할 때, 선수과목이 존재하고 수강시간이 주어졌을 때, 모든 강의를 수강하는데 걸리는 시간 구하기
# 이전 선수과목들에 대하여 가장 오래 걸리는 시간 t을 저장해놓으면 현재 과목을 듣는데 걸리는 시간 k일때, 총 걸리는 시간은 t + k이다.

from collections import deque

# 강의의 수 N 입력
n = int(input())
# 과목 당 차수 저장할 배열 생성
degree = [0] * (n + 1)
# 해당 과목을 선수과목으로 가지고 있는 정보 담기! 예) data[1] = [2,3] => 1을 수강해야 2,3을 들을 수 있다.
graph = [[] for _ in range(n + 1)]
# 강의별 수강시간 담을 배열 선언
times = [0] * (n + 1)
# 과목별 선수과목이 가장 오래 걸리는 시간 담아둘 배열
max_prev = [0] * (n + 1)

# 강의의 수만큼 정보 입력받기
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    # 첫번째 인덱스는 강의시간
    times[i] = info[0]
    # 첫번째, 마지막을 제외한 인덱스에는 선수과목의 정보가 들어가있다.
    for x in info[1:-1]:
        # 선수과목 x를 기준으로 i정보를 넣어주기
        graph[x].append(i)
        # i의 차수 올리기
        degree[i] += 1

# 여기까지 데이터 입력완료

q = deque([])
# 진입차수가 0인 친구 큐에 넣어주기
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q: # 큐가 빌 때까지
    now = q.popleft()
    # 현재 과목을 선수과목으로 가지고 있는 친구들 차수 1 빼주기
    for i in graph[now]:
        degree[i] -= 1
        # 또한 최고로 오래 걸리는 선수과목으로 갱신해주기
        max_prev[i] = max(max_prev[i], times[now])
        # 진입 차수가 0이 된다면 큐에 넣어주기
        if degree[i] == 0:
            q.append(i)
            # 또한 0이 되는 시점에 이제 선수과목의 최장 시간을 구했으니 그대로 time에 넣어주기
            times[i] += max_prev[i]

# 각 강의의 최소 수강시간 출력하기
for i in range(1, n + 1):
    print(times[i])
