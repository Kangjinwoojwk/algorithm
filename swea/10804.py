T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
trans_key = {'b' : 'd',
       'p' : 'q',
       'd' : 'b',
       'q' : 'p'}
for test_case in range(1, T + 1):
    get_change = input()
    answer = ''
    for i in get_change:
        answer = trans_key[i] + answer
    print('#{} {}'.format(test_case, answer))
#