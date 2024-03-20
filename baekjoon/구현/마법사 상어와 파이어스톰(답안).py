from collections import deque

n, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(2 ** n)] # 얼음배열
command = list(map(int, input().split())) # L단계
visited = set() # 얼음덩어리 방문배열
# 인접 네방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
length = 2 ** n # 배열의 길이

# 격자 나눠서 회전시키기
def divide(a, c):
    cnt = 2 ** c # 격자의 길이
    for i in range(0, length, cnt):
        for j in range(0, length, cnt):
            temp = [] # 격자 임시 배열
            for k in range(cnt): # 격자의 길이만큼
                temp.append(a[i + k][j:j + cnt]) # 임시 배열 만들기
            temp = list(zip(*temp[::-1])) # 90도회전
            for k in range(cnt):
                a[i + k][j:j + cnt] = temp[k] # 원래 배열에 반영
    return a

# 얼음양 줄어들기
def reduce(a):
    temp = [[0] * length for _ in range(length)] # 임시배열
    for i in range(length):
        for j in range(length):
            cnt = 0 # 인접한 칸중 얼음이 있는 개수
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < length and 0 <= ny < length:
                    if a[nx][ny] > 0: #인접하고 얼음있으면
                        cnt += 1 # 카운트 증가
            if cnt <= 2 and a[i][j] > 0: # 카운트 2이하
                temp[i][j] -= 1 # 임시배열에 반영
    for i in range(length):
        for j in range(length):
            a[i][j] += temp[i][j]
    return a

# 얼음덩어리 개수세기
def bfs(x, y):
    q = deque()
    q.append((x, y)) # 큐에 저장
    visited.add((x, y)) # 방문
    cnt = 1 # 덩어리 개수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 안에 있고
            if 0 <= nx < length and 0 <= ny < length:
                if (nx, ny) not in visited and a[nx][ny] != 0:
                    q.append((nx, ny)) # 큐에 저장
                    visited.add((nx, ny))
                    cnt += 1
    return cnt

# 단계 실행
for c in command:
    a = divide(a, c)
    a = reduce(a)

answer = 0
max_ans = 0
for i in range(length):
    for j in range(length):
        if a[i][j] > 0:
            answer += a[i][j]
            max_ans = max(max_ans, bfs(i, j))

print(answer)
print(max_ans)
