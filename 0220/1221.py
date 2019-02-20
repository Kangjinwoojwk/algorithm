import sys
sys.stdin = open('1221.txt', 'r')
sys.stdout = open('1221_out.txt', 'w')
T = int(input())
for _ in range(T):
    test_case, n = list(input().split())
    n = int(n)
    result = {
        'ZRO': 0,
        'ONE': 0,
        'TWO': 0,
        'THR': 0,
        'FOR': 0,
        'FIV': 0,
        'SIX': 0,
        'SVN': 0,
        'EGT': 0,
        'NIN': 0
    }
    re = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    li = list(input().split())
    for i in range(n):
        result[li[i]] += 1
    i = j = 0
    print(test_case)
    while i < n:
        if result[re[j]] != 0:
            result[re[j]] -= 1
            print(re[j], end=' ')
            i += 1
        else:
            j += 1
    print()