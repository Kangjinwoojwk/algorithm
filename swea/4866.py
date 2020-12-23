import sys
sys.stdin = open('4866.txt', 'r')
sys.stdout = open('4866_out.txt', 'w')
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
                print(f'#{test_case} 0')
                break
            else:
                if (li[-1] == '(' and i == ')') or (li[-1] == '{' and i == '}') or (li[-1] == '[' and i == ']'):
                    li = li[:-1]
                else:
                    print(f'#{test_case} 0')
                    break
    else:
        if len(li) == 0:
            print(f'#{test_case} 1')
        else:
            print(f'#{test_case} 0')
