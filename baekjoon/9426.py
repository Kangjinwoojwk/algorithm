N, K = map(int, input().split())
data = [int(input()) for _ in range(N)]
chk = data[:K]
chk.sort()
ans = 0
for _ in range(N - K):
    ans += chk[(K - 1) // 2]
    for i in range(K):
        if data[_] == chk[i]:
            chk.pop(i)
            break
    for i in range(K - 1):
        if chk[i] > data[_ + K]:
            chk.insert(i, data[_ + K])
            break
    else:
        chk.append(data[_ + K])
ans += chk[(K - 1) // 2]
print(ans)