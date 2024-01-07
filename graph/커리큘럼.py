# 여러 선수과목이 존재할 때 어떤 것을 듣는 것이 제일 오래 걸리는지 파악하고 가장 오래 걸리는 시간 출력하기.
from collections import deque

# 과목개수 입력받기
n = int(input())
# 선수과목정보 넣어주기
graph = [[] for _ in range(n + 1)]
# 차수정보 넣어주기 시작은 0으로 초기화
degree = [0] * (n + 1)
times = [0] * (n + 1)
# 과목개수만큼 돌면서 선수과목 정보 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    # 수강시간 정보 넣어주기
    times[i] = data[0]
    # 만약 b의 선수과목이 a라면 graph[a].append(b) 형식으로 저장해놓고 b의 차수올려주기
    for j in range(1, len(data) - 1):
        graph[data[j]].append(i)
        degree[i] += 1

q = deque()
result = [0] * (n + 1)
# 차수가 0인 애들 큐에 넣어주기
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        # 선수과목이 없는 애들은 수강시간을 본인의 수강시간으로 초기화
        result[i] = times[i]

while q: # 큐가 빌때까지
    # 차수가 0인녀석 꺼내주기
    now = q.popleft()
    # 현재 과목을 선수과목으로 갖는 과목들 찾아서 차수내려주기
    for i in graph[now]:
        result[i] = max(result[i], result[now] + times[i])
        degree[i] -= 1
        # 차수가 0이 되었다면 큐에 넣어주기
        if degree[i] == 0:
            q.append(i)

# 가장 수강시간이 오래 걸리는 과목 출력
for i in range(1, n + 1):
    print(result[i])
