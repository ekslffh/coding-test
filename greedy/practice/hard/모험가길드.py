# n명의 모험가가 존재하고 각각 공포도를 가지고 있다. 공포도가 x라면 x이상의 그룹으로 짜져야 한다.
# 그룹 수의 최대값

# 최대한 많은 그룹을 만드려면 정렬하고 작은 순서대로 내보내는게 현명하다.

# 모험가 수 입력받기
n = int(input())

# n명의 모험가의 각각의 공포도 입력받고 오름차순 정렬
data = list(map(int, input().split()))
# 공포도가 작은 친구들부터 보낼볼겨
data.sort()

# 그룹 수
result = 0

start = 0
end = 0
while start < n:
    end = start
    while end < n and max(data[start : end + 1]) > (end - start + 1):
        end += 1
    if end >= n:
        break
    else:
        result += 1
        start = end + 1

print(result)
