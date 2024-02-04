# N개의 정수와 N - 1개의 연산자가 주어졌을 때, 결과의 최대값과 최소값 구하기

from itertools import permutations

# 정수의 개수(n) 입력받기
n = int(input())
# n개의 정수 입력받기
data = list(map(int, input().split()))
# n - 1개의 연산자 정보 입력받기 +, -, x, / 개수
plus, minus, multiply, divide = map(int, input().split())

options = ['+'] * plus + ['-'] * minus + ['x'] * multiply + ['/'] * divide
unique_permutations = set(permutations(options))
option_list = list(unique_permutations)

# 연산자에 따라 계산해주는 함수
def calc(a, b, opt):
    if opt == '+':
        return a + b
    elif opt == '-':
        return a - b
    elif opt == 'x':
        return a * b
    else:
        result = abs(a) // abs(b)
        # 양수, 음수 다르게 처리
        # 음수인 경우, 몫만 구하고 -를 붙여서 리턴하기
        if a < 0 or b < 0:
            return -1 * result
        else:
            return result

# option_list를 이요하여 결과를 내보고 가장 큰값과 작은 값 구해보기
answer = []
for ol in option_list:
    # 특정 경우의 연산자 리스트 보여줌.
    result = data[0]
    for i in range(1, len(data)):
        result = calc(result, data[i], ol[i - 1])
    answer.append(result)

print(max(answer))
print(min(answer))
