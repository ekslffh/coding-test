array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

array = [('바나나', 2), ('사과', 5), ('당근', 3)]
array.sort(key=lambda x: x[1])
print(array) # [('바나나', 2), ('당근', 3), ('사과', 5)]

array = [('바나나', 2), ('사과', 5), ('당근', 3)]
array.sort(key=lambda x: -x[1])
print(array) # [('사과', 5), ('당근', 3), ('바나나', 2)]

array = [('바나나', 2, 5), ('사과', 2, 4), ('당근', 3, 7)]
array.sort(key=lambda x: (x[1], x[2]))
print(array) # [('사과', 2, 4), ('바나나', 2, 5), ('당근', 3, 7)]

array = [('바나나', 2, 5), ('사과', 2, 4), ('당근', 3, 7)]
array.sort(key=lambda x: (x[1], -x[2]))
print(array) # [('바나나', 2, 5), ('사과', 2, 4), ('당근', 3, 7)]
