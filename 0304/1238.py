import sys
sys.stdin = open('1238.txt', 'r')
sys.stdout = open('1238_out.txt', 'w')
for test_case in range(1, 11):
    lenth_data, start = map(int, input().split())
    input_data = list(map(int, input().split()))
    contact = [True] * 101
    from_to_edge = [[] for _ in range(101)]
    for i in range(lenth_data // 2):
        from_to_edge[input_data[2 * i]].append(input_data[2 * i + 1])
    contact[start] = False
    queue = [from_to_edge[start], []]
    for i in from_to_edge[start]:
        contact[i] = False
    while queue[0] != []:
        for i in queue[0]:
            for j in from_to_edge[i]:
                if contact[j]:
                    queue[1].append(j)
                    contact[j] = False
        if queue[1] == []:
            N = len(queue[0])
            ans = queue[0][0]
            for i in range(N):
                if ans < queue[0][i]:
                    ans = queue[0][i]
        queue[0][:] = queue[1][:]
        queue[1] = []
    print('#{} {}'.format(test_case, ans))




