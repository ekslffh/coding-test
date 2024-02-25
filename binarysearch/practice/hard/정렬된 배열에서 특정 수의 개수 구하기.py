# 시작점, 끝점 둘다 이진탐색을 통해서 찾아야 함.

n, x = map(int, input().split())

data = list(map(int, input().split()))

# 시작점, 끝점 초기화
start = n
end = -1

# 재귀함수
def recursion(s, e, target):
    global start, end
    if s > e:
        return
    mid = (s + e) // 2
    # 만약 중간값이 타겟값이라면 왼쪽 오른쪽 둘다 탐색하여서 시작점, 끝점 구하기
    if data[mid] == target:
        start = min(start, mid)
        end = max(end, mid)
        recursion(s, mid - 1, target)
        recursion(mid + 1, e, target)
    # 만약 중간값이 타겟보다 크다면 중간값 - 1부터 다시 탐색
    elif data[mid] > target:
        recursion(s, mid - 1, target)
    # 만약 중간값이 타겟보다 작다면 중간값 + 1부터 다시 탐색
    else:
        recursion(mid + 1, e, target)

recursion(0, n - 1, x)

if start == n:
    print(-1)
else:
    print(end - start + 1)
