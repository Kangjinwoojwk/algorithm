T = int(input())

for test_case in range(1, T + 1):
    open_set = {'{', '(', '['}
    close_set = {'}', ')', ']'}
    li = []
    get_data = input()
    for i in get_data:
        if i in open_set:
            li.append(i)
        elif i in close_set:
            if len(li) == 0:
                print(f'#{test_case} False')
                break
            else:
                if (li[-1] == '(' and i == ')') or (li[-1] == '{' and i == '}') or (li[-1] == '[' and i == ']'):
                    li = li[:-1]
                else:
                    print(f'#{test_case} False')
                    break
    else:
        if len(li) == 0:
            print(f'#{test_case} True')
        else:
            print(f'#{test_case} False')
