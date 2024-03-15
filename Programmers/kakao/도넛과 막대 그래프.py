from collections import deque
import copy

def solution(edges):
    answer = []
    donut_cnt, bar_cnt, graph_cnt = 0, 0, 0

    # 간선정보 data에 정리하기 data[a] = [a가 가리키는 노드 리스트]
    data = {}
    for a, b in edges:
        if a not in data:
            data[a] = [b]
        else:
            data[a].append(b)

    # data중 최대값을 찾아서 배열 만들어주기
    n = max(data.keys())

    # 임의의 정점 찾기 : 아무도 자신을 향하지 않는 정점
    vertex = 0
    for x in data.keys():
        is_find = True
        for key in data.keys():
            if x in data[key]:
                is_find = False
                break
        if is_find:
            vertex = x
            break

    # 정점을 기준으로 각 그래프 파악해보기
    visited = [False] * (n + 1)
    for x in data.keys():
        pre_visited = copy.copy(visited)

        # 임의의 정점은 넘어가기
        if x == vertex:
            continue
        # 방문한 곳 넘어가기
        if visited[x]:
            continue
        # 방문 처리
        visited[x] = True
        q = deque([x])
        # 순환여부
        is_cycle = False
        # 노드와 간선의 개수를 세보기
        node_cnt, edge_cnt = 0, 0
        path = []
        while q:
            now = q.popleft()
            path.append(now)
            node_cnt += 1
            # 연결정보가 없는 경우 처리해주기 (bar인 경우만 그럴듯)
            if now not in data:
                continue
            # 연결된 간선으로 큐에 넣어주기
            for a in data[now]:
                edge_cnt += len(data[now])
                if not visited[a]:
                    q.append(a)
                    visited[a] = True
                else:
                    if not pre_visited[a]:
                        is_cycle = True
        if is_cycle:
            if node_cnt == edge_cnt:
                donut_cnt += 1
            else:
                graph_cnt += 1

    # 여기까지 왔을 때, 정점, 도넛, 그래프까지 구함
    bar_cnt = len(data[vertex]) - (donut_cnt + graph_cnt)

    answer = [vertex, donut_cnt, bar_cnt, graph_cnt]

    return answer
