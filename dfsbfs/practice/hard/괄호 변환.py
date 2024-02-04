# u, v로 분리하는 함수
def seperate_p(p):
    # 열리고 닫는 괄호 개수 세기
    open_cnt = 0
    close_cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_cnt += 1
        else: # ')'인 경우
            close_cnt += 1
        # 최초로 두개가 같아지는 경우가 더이상 분리되지 않는 균형잡힌 문자열 u가 된다.
        if open_cnt == close_cnt:
            # (u, v) 형태로 리턴하기 + 현재인덱스까지 포함되어야 함.
            return (p[:i + 1], p[i + 1:])

# 올바른 문자열인지 판단하는 함수
def check_correct(u):
    # 닫히는 부분에서 열린 태그 개수와 일치해야 함.
    open_cnt = 0
    close_cnt = 0
    for i in range(len(u)):
        if u[i] == '(':
            open_cnt += 1
            # 닫힌 태그일 때 먼저 close_cnt에 1더해주고 개수 비교해보기
        elif u[i] == ')':
            close_cnt += 1
            # 닫는 태그가 여는 태그보다 개수가 많아지면 올바르지 않은 문자열로 False 리턴하기
            if open_cnt < close_cnt:
                return False
    # 모든 구간을 무사히 넘기면 True 리턴 (올바른 문자열임)
    return True

# 받은 문자열을 처음과 끝을 삭제하고 뒤집는 함수
def remove_and_flip(t):
    result = ''
    # 처음과 끝을 제외하고 반대로 뒤집기
    for i in range(1, len(t) - 1):
        if t[i] == '(':
            result += ')'
        else:
            result += '('
    return result

def recursion_conversion(p):
    # p가 빈문자열이라면 그대로 반환하기
    if p == '':
        return ''
    # 1. u, v로 분리하기
    u, v = seperate_p(p)
    # 2. u가 올바른 문자열인지 판단하기
    if check_correct(u):
        # 2-1. 올바른 문자열이라면 그대로 u에다가 v를 재귀돌린 결과를 더해서 리턴
        return u + recursion_conversion(v)
    else: # 2-3. 올바른 문자열이 아니라면 프로세스대로 변환하기
        # a. 빈문자열을 준비한다.
        temp = ''
        # b. '(' + v를 재귀돌린 값 + ')' + u의 중간문자들을 방향을 뒤집어서 붙이기
        return '(' + recursion_conversion(v) + ')' + remove_and_flip(u)

def solution(p):
    answer = recursion_conversion(p)
    return answer
