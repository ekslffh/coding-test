import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur_node, pre_node):
    # cnt, d 둘다 함수 외부에 존재하지만, d 는 단순히 읽기용이고, cnt 는 값을 수정해야 하므로 global 설정을 해준다.
    global cnt
    max_d = 0
    for next_node in graph[cur_node]:
        if next_node != pre_node:
            max_d = max(max_d, dfs(next_node, cur_node))
    if max_d >= d:
        cnt += 1
    return max_d + 1

n, s, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
dfs(s, 0)
print((cnt - 1) * 2 if cnt else 0)
