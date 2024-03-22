import sys

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
leng = len(b)

stack = []
for x in a:
    stack.append(x)
    if stack[len(stack) -leng: len(stack)] == b:
        for _ in range(leng):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print('FRULA')
