# # 1. 내풀이
# # 배열의 크기 N, 숫자가 더해지는 횟수 M, 하나의 인덱스의 숫자가 연속으로 더해질 수 있는 최대 횟수 K
# # N, M, K 입력받기
# n, m, k = map(int, input().split())
# # N개의 숫자 데이터 입력받기
# data = list(map(int, input().split()))
# # 데이터 내림차순 정렬
# data.sort(reverse=True)
# # 가장 큰수는 0인덱스, 두번째는 1인덱스에 존재한다.
# first, second = data[0], data[1]
# # 세트로 보면 first k개 + second 한개 -> (k + 1)개
# # 그러면 M // (k + 1) 이 세트가 나오는 개수
# cal_cnt = m // (k + 1)
# # M % (k + 1)개가 나머지 first로 나열하면 된다.
# rest_cnt = m % (k + 1)
# # 정답 도출
# result = (first * k + second) * cal_cnt + first * rest_cnt
# # 정답출력하기
# print(result)

# # 2. 책풀이
# # N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))
#
# data.sort() # 입력받은 수를 정렬하기
# first = data[n - 1] # 가장 큰 수
# second = data[n - 2] # 두 번째로 큰수
#
# result = 0
#
# while True:
#     for i in range(k): # 가장 큰 수를 K번 더하기
#         if m == 0: # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1 # 더할 때마다 1씩 빼기
#     if m == 0: # m이 0이라면 반복문 탈출
#         break
#     result += second # 두번째로 큰 수를 한번 더하기
#     m -= 1 # 더할 때마다 1씩 빼기
#
# print(result) # 최종 답안 출력

# 3. 책풀이2 (반복되은 수열을 파악하여 횟수 구해보기)
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기

print(result) # 최종 답안 제출
