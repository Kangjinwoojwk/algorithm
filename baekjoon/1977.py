square = [False] * 10001
for i in range(101):
    square[i ** 2] = True
N = int(input())
M = int(input())
value = 0
mini = 0
for i in range(N, M + 1):
    if square[i]:
        value += i
        if mini == 0:
            mini = i
if value == mini == 0:
    print(-1)
else:
    print(value)
    print(mini)