import heapq
import sys
input = sys.stdin.readline

# 강의 개수 N개 입력
n = int(input())
# N개의 강의 정보 입력 - 시작 시간: s, 종료 시간: t
data = []
for _ in range(n):
    s, t = map(int, input().split())
    data.append((s, t))
# 강의들 정렬 : 종료 시간 asc & 시작 시간 asc
data.sort(key=lambda x: (x[0], x[1]))
# 제일 먼저 끝나는 강의 최소힙에 넣기
q = []
# 최소힙으로 (끝나는 시간, 시작 시간) 으로 넣어주기
heapq.heappush(q, (data[0][1], data[0][0]))
# 두번째 강의부터 모든 강의 돌면서 검사하기
for i in range(1, n):
    # 가장 빨리 끝나는 강의 꺼내서 현재 강의를 들을 수 있는지 검사
    pt, ps = heapq.heappop(q)
    cs, ct = data[i]
    # 들을 수 있다면, 종료 시간을 업데이트해서 다시 최소 힙에 넣기
    if pt <= cs:
        # + 가장 간격이 좁은 강의실로 배정받기
        heapq.heappush(q, (ct, ps))
    # 들을 수 없다면, 강의실을 새로 파서 최소힙에 넣어주기
    else:
        # 원래 강의도 넣어줘야 함.
        heapq.heappush(q, (pt, ps))
        heapq.heappush(q, (ct, cs))

# 결과적으로, 최소힙에 들어있는 개수가 강의실의 개수가 된다.
print(len(q))

# 가장 간격이 좁게 붙이기 위해서는 가장 먼저 시작하는 강의부터 순서대로 연결시켜봐야 한다.
