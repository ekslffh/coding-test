# n, m, k = map(int, input().split())
#
# # 모든 상어의 위치와 방향 정보를 포함하는 2차원 리스트
# array = []
# for i in range(n):
#     array.append(list(map(int, input().spllit())))
#
# # 모든 상어의 현재 방향 정보
# directions = list(map(int, input().split()))
#
# # 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
# smell = [[[0, 0]] * n for _ in range(n)]
#
# # 각 상어의 회전 방향 우선순위 정보
# priorities = [[] for _ in range(m)]
# for i in range(m):
#     for j in range(4):
#         priorities[i].append(list(map(int, input().split())))
#
# # 특정 위치에서 이동 가능한 4가지 방향
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# # 모든 냄새 정보를 업데이트
# def update_smell():
#     # 각 위치를 하나씩 확인하며
#     for i in range(n):
#         for j in range(n):
#             # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
#             if smell[i][j][1] > 0:
#                 smell[i][j][1] -= 1
#             # 상어가 존재하는 해당 위치의 냄새를 k로 설정
#             if array[i][j] != 0:
#                 smell[i][j] = [array[i][j], k]
#
# # 모든 상어를 이동시키는 함수
# def move():
#     # 이동 결과를 담기 위한 임시 결과 테이블 초기화
#     new_array = [[0] * n for _ in range(n)]
#     # 각 위치를 하나씩 확인하며
#     for x in range(n):
#         for y in range(n):
#             # 상어가 존재하는 경우
#             if array[x][y] != 0:
#                 direction = directions[array[x][y] - 1] # 현재 상어의 방향
#                 found = False
#                 # 일단 냄새가 존재하지 않는 곳이 있는지 확인
#                 for index in range(4):
