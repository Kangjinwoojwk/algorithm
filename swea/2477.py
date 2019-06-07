for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    t = [0] + list(map(int, input().split()))
    customer = 0
    customerRecord = [[0, 0]for _ in range(K + 1)]
    await = list()
    bwait = list()
    acustomer = [[0, 0]for _ in a]
    bcustomer = [[0, 0]for _ in b]
    ti = 0
    while customer != K:
        for i in range(1, K + 1):
            if t[i] > ti:
                break
            if t[i] == ti:
                await.append(i)
        for i in range(1, N + 1):
            if acustomer[i][1] == 0 and await:
                acustomer[i][0] = a[i]
                acustomer[i][1] = await.pop(0)
                customerRecord[acustomer[i][1]][0] = i
            if acustomer[i][0]:
                acustomer[i][0] -= 1
            if acustomer[i][0] == 0 and acustomer[i][1]:
                bwait.append(acustomer[i][1])
                acustomer[i][1] = 0
        for i in range(1, M + 1):
            if bcustomer[i][1] == 0 and bwait:
                bcustomer[i][0] = b[i]
                bcustomer[i][1] = bwait.pop(0)
                customerRecord[bcustomer[i][1]][1] = i
            if bcustomer[i][0]:
                bcustomer[i][0] -= 1
            if bcustomer[i][0] == 0 and bcustomer[i][1]:
                customer += 1
                bcustomer[i][1] = 0
        ti += 1
    ans = 0
    for i in range(1, K + 1):
        if customerRecord[i][0] == A and customerRecord[i][1] == B:
            ans += i
    if ans == 0:
        ans = -1
    print('#{} {}'.format(tc, ans))