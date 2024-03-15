# 컨베이어 벨트 위의 로봇

from collections import deque

n, k = map(int, input().split())
conveyor_belt = deque(list(map(int, input().split())))

# 벨트의 끝 칸에 도달했을 때, 첫번째 공간으로 순환 시켜주는 함수
def rotation(now):
    global n
    if now == (2 * n - 1):
        return 0
    else:
        return now + 1

# 컨베이어 벨트 동작
def operate(n, k, conveyor_belt):
    robots = deque([])
    stage = 0
    while True:
        stage += 1
        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        # 컨베이어 벨트 회전 : 끝에 원소를 맨 앞으로 가져오기
        last = conveyor_belt.pop()
        conveyor_belt.appendleft(last)
        # 로봇 같이 이동 : 순서대로 꺼내서 다음 곳으로 이동시키기
        next_robots = []
        while robots:
            now = robots.popleft()
            next_step = rotation(now)
            # 내리는 지점
            if next_step == (n - 1):
                continue
            # 다음 로봇 위치 배열 넣어주기
            next_robots.append(next_step)
        # 로봇 위치 갱신
        robots = deque(next_robots)
        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
            # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        next_robots = []
        while robots:
            # 로봇을 순서대로 다음 스텝으로 이동 해보기
            now = robots.popleft()
            next_step = rotation(now)
            # 다음 칸으로 이동할 수 있는 경우
            # 1. 이동하려는 칸에 로봇이 없어야 함, 2. 해당 칸이 내구도가 1 이상 이어야 한다.
            if next_step not in robots and next_step not in next_robots and conveyor_belt[next_step] >= 1:
                # 내구도 깎기
                conveyor_belt[next_step] -= 1
                # 내리는 지점
                if next_step == (n - 1):
                    continue
                next_robots.append(next_step)
            # 이동할 수 없는 경우, 그대로 있는다.
            else:
                next_robots.append(now)
        # 로봇 정보 갱신
        robots = deque(next_robots)
        # 3. 올리는 위치에 로봇이 없고 내구도가 1 이상이라면 올리기
        if 0 not in robots and conveyor_belt[0] >= 1:
            robots.append(0)
            conveyor_belt[0] -= 1
        # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
        if conveyor_belt.count(0) >= k:
            break
    return stage

print(operate(n, k, conveyor_belt))
