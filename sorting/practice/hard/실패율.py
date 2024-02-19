# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# def solution(N, stages):
#     answer = []
#
#     # 스테이지 수만큼 배열 만들어서 현재 라운드에 머물러 있는 사람들 체크하기
#     cnt = len(stages)
#
#     # n + 1까지 도달하면 올 클리어한 사람이다.
#     data = [0] * (N + 2)
#     for stage in stages:
#         data[stage] += 1
#
#     # 각 스테이지 별로 실패율 측정해보기
#     result = []
#     for stage in range(1, N + 1):
#         # 실패율 = 현재 스테이지 머물러있는 사람 / 스테이지에 도달한 사람
#         ## 스테이지에 도달한 사람이 없다면 0으로 정의하기
#         if cnt == 0:
#             result.append((0, stage))
#             continue
#         failure = data[stage] / cnt
#         # (실패율, 스테이지) 형식으로 저장하기
#         result.append((failure, stage))
#         # 다음 스테이지에 cnt는 현재 여기 머물러있는 사람은 빼야한다.
#         cnt -= data[stage]
#
#     # 실패율 기준으로 내림차순 정렬하기 + 실패율이 같다면 작은 번호부터(오름차순)
#     result.sort(reverse=True, key=lambda x: (x[0], -x[1]))
#
#     # 정렬순서대로 스테이지 정보 저장하기
#     for r in result:
#         answer.append(r[1])
#
#     return answer
