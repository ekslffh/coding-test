# from itertools import permutations
#
# def solution(n, weak, dist):
#     answer = -1
#
#     # 오름차순 정렬
#     dist.sort(reverse=True)
#
#     # 반시계로 갈수도 있기 때문에 맵 확장하기. [a, b, c, 12 + a, 12 + b, 12 + c]
#     expand_weak = weak + [x + n for x in weak]
#
#     # 1명부터 최대인원까지 보내보기 (완전탐색)
#     for person in range(1, len(dist) + 1):
#         # 투입인원 선정 (실력 좋은 애들부터 데려오기)
#         in_dist = dist[:person]
#         rnd_dist = permutations(in_dist, person)
#         # 확장맵을 앞에서부터 취약점 개수만큼 반복한다. [a,b,c,d] ~ [d,a+n,b+n,c+n]까지
#         for i in range(len(weak)):
#             # 현재 취약점 이동경로 구하기
#             cur_weak = expand_weak[i:i + len(weak)]
#             # 현재 취약점 경로대로 투입인원 보내보기
#             cur_idx = 0
#             cnt = 1
#             for rd in rnd_dist:
#                 for j in range(len(rd)):
#                     sum = 0
#                     while cur_idx < len(cur_weak) - 1:
#                         d = cur_weak[cur_idx + 1] - cur_weak[cur_idx]
#                         if (rd[j] - sum) >= d:
#                             cur_idx += 1
#                             sum += d
#                             cnt += 1
#                         else:
#                             # 다음 투입할 인원이 있다면 위치를 다음 지점으로 옮기고 카운터도 세주기
#                             if (j + 1) < len(rd):
#                                 cur_idx += 1
#                                 cnt += 1
#                             # 투입할 인원이 없다면 반복문 나가기
#                             else:
#                                 break
#                 # 전부 다 성공적을 돌았을 경우를 바로 리턴하면 그게 점검인원의 최소값이 된다.
#                 if cnt == len(weak):
#                     return len(rd)
#
#     # 취약점 개수만큼 반복하면서 그만큼 잘라서 경로를 설정한다.
#
#     # 해당 인원으로 다 갈 수 있는지 확인해 보기
#
#     # 전체를 다 투입해도 못가면 -1 리턴
#
#     return answer

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer

# 특정 경로에 대한 친구들 투입순서도 고려해야함.
# 현재위치에 따른 투입인원의 최대 가능 거리를 계산해서 이동하는 방식으로 ㄱㄱ : 어렵다...
