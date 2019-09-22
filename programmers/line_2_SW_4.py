N = int(input())
seat = input().split()
cnt = 0
max_cnt = 0
for i in range(N):
    if seat[i] == '0':
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    else:
        cnt = 0
print((max_cnt + 1) // 2)