# 볼링공이 N개 주어지고 볼링공의 무게는 최대 M까지 이다.
# 두 사람이 다른 무게의 볼링공을 고를 경우의 수를 구하기

# # 풀이 1. 반복문을 이용하여 O(N**2) 경우의 수 구하기
# # 볼링공의 갯수 N, 무게 최대값 M 입력받기
# n, m = map(int, input().split())
# # 각각의 볼링공의 무게 입력받기
# data = list(map(int, input().split()))
# # 1번부터 돌면서 idx + 1에 대하여 자기와 무게가 다른 볼링공있는지 카운팅하기
# cnt = 0
# for i in range(n):
#     cur_w = data[i]
#     for j in range(i + 1, n):
#         # 현재 볼링공과 무게가 다르면 개수 세기
#         if cur_w != data[j]:
#             cnt += 1
# # 1번,2번과 2번,1번은 같은 경우로 생각하는 것
#
# # 정답 출력
# print(cnt)

# 풀이 2. 확통 공식과 계수정렬을 이용하여 정답 도출하기 O(M)
# 볼링공의 개수(N), 공의 최대 무게(M) 입력받기
n, m = map(int, input().split())
# 전체 볼링공 중 2개를 선택하는 경우의 수 구하기 nC2
a = int(n * (n - 1) / 2)
# N개의 볼링공의 무게(K) 입력받기
data = list(map(int, input().split()))
# 반복문 돌면서 M개의 리스트에 계수정렬 수행
sorted_data = [0] * (m + 1)
for d in data:
    sorted_data[d] += 1
# M개의 리스트에 대하여 개수가(x) 2개 이상일 때 xC2 수행하여 누적으로 더해주기
b = 0
for i in range(1, m + 1):
    if sorted_data[i] >= 2:
        cur_num = sorted_data[i]
        b += int(cur_num * (cur_num - 1) / 2)
# 전체 경우의 수 - 같은 공을 선택할 경우의 수 누적 = 정답
result = a - b
# 정답 출력하기
print(result)
