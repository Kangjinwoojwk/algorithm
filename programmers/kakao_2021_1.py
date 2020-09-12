def solution(new_id):
    # A65, Z90 a97 z122
    answer = ''
    possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.'
    not_possible = '~!@#$%^&*()=+[{]}:?,<>'
    for i in new_id:
        if i in possible:
            answer += i
    new_id = answer
    answer = ''
    for i in new_id:
        if 65 <= ord(i) <= 90:
            answer += chr(ord(i) + 32)
        else:
            answer += i
    new_id = answer
    answer = ''
    chk = False
    for i in new_id:
        if i == '.':
            if chk:
                continue
            chk = True
        else:
            chk = False
        answer += i

    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer = 'a'
    answer = answer[0:15]
    while answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))
    return answer