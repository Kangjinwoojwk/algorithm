T = int(input())
for test_case in range(1, T + 1):
    score = list(map(int, input().split()))
    for i in range(5):
        if score[i] < 40:
            score[i] = 40
    answer = sum(score)//5
    print('#{} {}'.format(test_case, answer))