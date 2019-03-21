T = int(input())
ori = input()
ans = 0
ori_cnt = [0] * 26
for i in ori:
    ori_cnt[ord(i) - ord('A')] += 1
for _ in range(T - 1):
    get = input()
    get_cnt = [0] * 26
    for i in get:
        get_cnt[ord(i) - ord('A')] += 1
    cnt = 0
    for i in range(26):
        cnt += abs(get_cnt[i] - ori_cnt[i])
    if cnt <= 2 and abs(len(ori) - len(get)) <= 1:
        ans += 1
print(ans)