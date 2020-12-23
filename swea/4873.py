import sys
sys.stdin = open('4873.txt', 'r')
sys.stdout = open('4873_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    get_str = input()
    li = []
    for i in get_str:
        if len(li) > 0:
            if i == li[-1]:
                li = li[:-1]
            else:
                li.append(i)
        else:
            li.append(i)
    print(f'#{test_case} {len(li)}')