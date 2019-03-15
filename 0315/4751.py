T = int(input())
for tc in range(1, T + 1):
    string = input()
    N = len(string)
    for i in range(N):
        print('..#.', end='')
    print('.')
    for i in range(N * 2):
        print('.#', end='')
    print('.')
    for i in range(N):
        print('#.'+string[i]+'.', end='')
    print('#')
    for i in range(N * 2):
        print('.#', end='')
    print('.')
    for i in range(N):
        print('..#.', end='')
    print('.')