import sys
sys.stdin = open('4839.txt', 'r')
sys.stdout = open('4839_out.txt', 'w')


def binary_search(start_page, end_page, target_page, cnt):
    temp = (start_page + end_page) // 2
    if temp == target_page:
        return cnt + 1
    elif temp > target_page:
        return binary_search(start_page, temp, target_page, cnt + 1)
    else:
        return binary_search(temp, end_page, target_page, cnt + 1)


T = int(input())
for test_case in range(1, T + 1):
    P, A, B = list(map(int, input().split()))
    a = binary_search(1, P, A, 0)
    b = binary_search(1, P, B, 0)
    if a == b:
        print(f'#{test_case} 0')
    elif a > b:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} A')
