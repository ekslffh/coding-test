word = input()

answer = {}

for x in word:
    x = x.upper()
    if x in answer.keys():
        answer[x] += 1
    else:
        answer[x] = 1

sorted_dict = sorted(answer.items(), key=lambda item: item[1], reverse=True)

if len(sorted_dict) > 1 and sorted_dict[0][1] == sorted_dict[1][1]:
    print('?')
else:
    print(sorted_dict[0][0])
