for tc in range(1, int(input()) + 1):
    price, cnt = input().split()
    cnt = int(cnt)
    price = list(price)
    N = len(price)
    i = 0
    pre = 0
    pre_idx = list()
    while cnt:
        j = N - 1
        for k in range(N - 1, i, -1):
            if price[k] > price[j]:
                j = k
        if i == N - 2:
            if price[i] == price[i - 1] and cnt > 1:
                price[i - 1: i + 2].sort()
                cnt = 0
                continue
            price[i], price[j] = price[j], price[i]
            cnt -= 1
            continue
        if price[i] >= price[j]:
            i += 1
            continue
        else:
            price[i], price[j] = price[j], price[i]
            if pre != price[i]:
                if len(pre_idx) > 1:
                    pre_idx.sort()
                    temp = [price[k] for k in pre_idx]
                    temp.sort(reverse=True)
                    for i in range(len(temp)):
                        price[pre_idx[i]] = temp[i]
                pre = price[i]
                pre_idx = [j]
            else:
                pre_idx.append(j)
            cnt -= 1
            i += 1
    if len(pre_idx) > 1:
        pre_idx.sort()
        temp = [price[k] for k in pre_idx]
        temp.sort(reverse=True)
        for i in range(len(temp)):
            price[pre_idx[i]] = temp[i]

    print('#{} {}'.format(tc, ''.join(price)))