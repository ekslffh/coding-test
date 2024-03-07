# N개의 팀이 있고, 작년의 순위 정보를 알고있을 때, 올해 두팀의 상대 순위가 바뀐 것에 대해서 정보가 제공된다.
# 이때, 올해 순위를 예측하여 1등팀부터 순서대로 출력하기 단, 순위를 예측 못한다면 IMPOSSIBLE 출력
import sys

# 테스트 케이스 개수 입력
t = int(input())

for _ in range(t):
    # 팀의 수 N 입력받기
    n = int(input())
    # 작년 순위 정보 입력 (1등팀부터 순서대로 팀번호 입력받기)
    prev_rank = list(map(int, input().split()))

    # 딕셔너리로 (팀 : 순위) 형태로 저장하기
    prev_dict = {}
    for i in range(n):
        prev_dict[prev_rank[i]] = i + 1

    # 상대적인 순위가 바뀐 쌍의 수 M 입력받기
    m = int(input())
    # 바뀐정보 입력 (a와 b의 상대적인 등수가 바뀌었다.)
    data = []
    for _ in range(m):
        a, b = map(int, input().split())
        data.append((a, b))

    # 해당 정보들을 이용하여 올해의 순위 맞추기

    # 자신보다 잘 본 팀 저장 배열
    up = [[] for _ in range(n + 1)]
    # 자신보다 못 본 팀 저장 배열
    down = [[] for _ in range(n + 1)]

    # data를 이용하여서 상대적인 순위가 바뀐 정보부터 처리해보기
    for d in data:
        a, b = d
        a_rank = prev_dict[a]
        b_rank = prev_dict[b]
        # 두 팀의 작년 순위를 비교해서 역전시키기
        # 작년의 a가 더 잘봤을 경우,
        if a_rank < b_rank:
            # 올해는 a가 더 못본것
            up[a].append(b)
            down[b].append(a)
        # b가 더 잘 봤을 경우
        else:
            # 올해는 b가 더 못봄
            up[b].append(a)
            down[a].append(b)

    # 이제는 작년 순위로 비교하기 (1팀부터 채우기)
    for team in range(1, n + 1):
        # 작년 순위 가져오기
        p_rank = prev_dict[team]
        # prev_rank에서 [:p_rank - 1]까지는 나보다 잘본팀, [p_rank:]는 나보다 못본팀
        # 정보를 넣어주는데 만약 이미 up이나 down에 들어가 있다면, pass
        # 더 잘본팀에 대하여
        for win_team in prev_rank[:p_rank - 1]:
            # 순위가 역전되었다면 자신의 down배열에 들어가 있을 것이다.
            if win_team not in down[team]:
                # 그게 아니라면, up쪽에 넣어주기
                up[team].append(win_team)
        # 더 못본 팀에 대하여
        for lose_team in prev_rank[p_rank:]:
            # 순위가 역전되었다면 자신의 up배열에 들어가 있기에 검사해보기
            if lose_team not in up[team]:
                down[team].append(lose_team)

    # 이제 up을 기준으로 순위를 매겨보자
    result = [0] * (n + 1)
    is_error = False
    # 1팀부터 순위 매겨보기
    for team in range(1, n + 1):
        # 특정 팀에 대하여 검사된 상위팀의 개수와 하위팀의 개수는 N - 1개여야 성립한다. 그게 아니라면 ? 출력하고 시스템 종료
        # if len(up[team]) + len(down[team]) < n - 1:
        #     is_error = True
        #     result = "?"
        # 순위는 상위 팀 개수 + 1
        rank = len(up[team]) + 1
        # 만약에 이미 결과에 해당 등수에 팀이 들어있다면 잘못된 계산이 된것이다.
        if result[rank] != 0:
            # IMPOSSIBLE 출력하고 시스템 종료
            is_error = True
            result = "IMPOSSIBLE"
            break
        else:
            # 그게 아니라면 해당 팀을 순위에 넣어주기
            result[rank] = team

    # 에러가 발생했다면 메시지 출력
    if is_error:
        print(result)
    # 그게 아니라면 정답 출력
    else:
        # 순위 출력하기 1등부터 ~ N등까지
        for i in range(1, n + 1):
            print(result[i], end=' ')
        print()
