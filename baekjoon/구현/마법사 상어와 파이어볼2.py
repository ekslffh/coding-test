n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
fireballs = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    graph[r - 1][c - 1].append((m, s, d))

steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def move():
    global n, graph
    temp_graph = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for m, s, d in graph[x][y]:
                dx = steps[d][0] * (s % n)
                dy = steps[d][1] * (s % n)
                nx = x + dx
                ny = y + dy
                if nx < 0:
                    nx += n
                elif nx >= n:
                    nx -= n
                if ny < 0:
                    ny += n
                elif ny >= n:
                    ny -= n
                temp_graph[nx][ny].append((m, s, d))
    for x in range(n):
        for y in range(n):
            if len(temp_graph[x][y]) >= 2:
                m_sum, s_sum = 0, 0
                is_odd, is_even = True, True
                for m, s, d in temp_graph[x][y]:
                    m_sum += m
                    s_sum += s
                    if d % 2 == 0:
                        is_odd = False
                    else:
                        is_even = False
                m_avg = m_sum // 5
                if m_avg == 0:
                    temp_graph[x][y] = []
                    continue
                s_avg = s_sum // len(temp_graph[x][y])
                if is_odd or is_even:
                    temp_graph[x][y] = [(m_avg, s_avg, d_val) for d_val in range(8) if d_val % 2 == 0]
                else:
                    temp_graph[x][y] = [(m_avg, s_avg, d_val) for d_val in range(8) if d_val % 2 != 0]
    graph = temp_graph

for _ in range(k):
    move()

answer = 0
for x in range(n):
    for y in range(n):
        for m, s, d in graph[x][y]:
            answer += m
print(answer)
