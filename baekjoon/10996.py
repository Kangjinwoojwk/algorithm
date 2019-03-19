N = int(input())
li = [['*' if i%2 == j%2 else ' ' for j in range(N)] for i in range(2 * N)]
for i in li:
    print(''.join(i))