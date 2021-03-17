T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    get_string = input()
    cnt_dict = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
        'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
        'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
        's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
        'y': 0, 'z': 0}
    for i in get_string:
        cnt_dict[i] += 1
    answer = ''.join([k for k, v in cnt_dict.items() if v % 2])
    if not answer:
        answer = 'Good'

    print('#{} {}'.format(test_case, answer))
