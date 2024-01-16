score = list(map(int, input()))

mid = len(score) // 2
left = sum(score[:mid])
right = sum(score[mid:])

if left == right:
    print("LUCKY")
else:
    print("READY")
