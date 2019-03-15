T = int(input())
for tc in range(1, T + 1):
    string = input()
    ans = 0
    for i in range(10, 0, -1):
        if string[0:i] == string[i:2 * i]:
            ans = i
    print('#{} {}'.format(tc, ans))