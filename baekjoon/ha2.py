from itertools import product
from collections import deque

def solution(N, number):
    options = ['+', '-', '*', '/', '&']

    def calc(sik, options):
        concat = []
        q = deque(sik)
        while q:
            now = q.popleft()
            if now != '&':
                concat.append(now)
            else:
                prev = concat.pop()
                next = q.popleft()
                dap = int(str(prev) + str(next))
                concat.append(dap)
        sik = concat
        result = sik[0]
        for i in range(len(sik) - 1):
            if sik[i] in options:
                if sik[i] == '+':
                    result += int(sik[i + 1])
                elif sik[i] == '-':
                    result -= int(sik[i + 1])
                elif sik[i] == '*':
                    result *= int(sik[i + 1])
                elif sik[i] == '/':
                    result //= int(sik[i + 1])
        return result

    for i in range(1, 10):
        for x in product(options, repeat=i-1):
            a = [N]
            for k in range(i - 1):
                a.append(x[k])
                a.append(N)
            if calc(a, options) == number:
                return i
            a[0] = N * - 1
            if calc(a, options) == number:
                return i
    return -1

print(solution(5, 12))
