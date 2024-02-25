# 고정점이란, 인덱스 = 해당값
# 오름차순 수열이 존재할 때 고정점이 있다면 해당 인덱스 출력, 없으면 -1 출력 (고정점은 최대 1개)
# logN으로 알고리즘 설계 -> 이진탐색

n = int(input())

data = list(map(int, input().split()))

answer = -1

def recursion(start, end):
    global answer
    if start > end:
        return
    idx = (start + end) // 2
    val = data[idx]
    # 인덱스 = 값이라면 정답출력
    if idx == val:
        answer = idx
        return
    # 인덱스가 값보다 큰 경우,
    # 1. 왼쪽 검사는 val - 1부터 하면된다.
    # 2. 오른쪽 검사는 idx + 1부터 진행
    elif idx > val:
        recursion(start, val - 1)
        recursion(idx + 1, end)
    # 인덱스가 값보다 작은 경우,
    # 1. 왼쪽 검사는 idx - 1부터 하면된다.
    # 2. 오른쪽 검사는 val + 1부터 진행
    else:
        recursion(start, idx - 1)
        recursion(val + 1, end)

# 0 ~ n -1로 검사 시작
recursion(0, n - 1)

# 정답출력 (없으면 -1 출력)
print(answer)
