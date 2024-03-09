# ac문자열을 R(뒤집기), D(첫번째 원소 삭제)연산을 수행한 결과 출력하기

# 문자열 -> 배열
def decode(data):
    # 데이터가 하나도 없다면, 빈 리스트 리턴
    if data == '[]':
        return []
    # 그게 아니라면, 앞뒤 문자 제거하고 ','로 잘라서 배열 만들기
    else:
        return data[1:-1].split(',')

# 배열 -> 문자열
def encode(data):
    result = '['
    for i in range(len(data)):
        result += data[i]
        # 마지막 원소가 아니라면 ',' 붙여주기
        if i < len(data) - 1:
            result += ','
    result += ']'
    return result

# 정답 담아줄 배열
answer = []
# 테스트 케이스 수만큼 반복하기
for _ in range(int(input())):
    # 수행할 함수 p 입력 ('RDDRR')
    p = list(input())
    # 배열의 정보 입력
    n = int(input())
    data = decode(input())
    # 배열의 길이보다 'D'연산이 더 많다면, error 출력
    if p.count('D') > len(data):
        answer.append('error')
        continue
    # 뒤집기 횟수
    r_cnt = 0
    # 뒤집기 횟수에 따른 앞,뒤 어디 자를지 결정
    f_cnt = 0
    b_cnt = 0
    for x in p:
        if x == 'D':
            # 뒤집기가 짝수 번 이루어졌다면, 앞에 자르기
            if r_cnt % 2 == 0:
                f_cnt += 1
            # 뒤집기가 홀수 번 이루어졌다면, 뒤에 자르기
            else:
                b_cnt += 1
        # 뒤집기 횟수 올려주기
        elif x == 'R':
            r_cnt += 1
    # 연산 정보에 따라서 문자열[앞자르기횟수:문자열길이 - 뒤자르기횟수]로 한번에 자르기
    data = data[f_cnt:n - b_cnt]
    # 뒤집기가 홀수번이라면, 뒤집고 정답 출력하기
    if r_cnt % 2 == 1:
        data.reverse()
    answer.append(encode(data))

# 저장된 정보들 순서대로 출력하기
for x in answer:
    print(x)
