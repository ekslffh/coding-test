def solution(number):
    answer = ''
    for x in str(number):
        answer += x + ','
    answer = answer[0:-1]
    print(answer)

solution(98765432)
