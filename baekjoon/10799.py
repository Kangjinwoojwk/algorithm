ans = 0
cnt = 0
pre = ''
for i in input():
    if i == '(':
        cnt += 1
    elif i == ')':
        if pre == '(':
            cnt -= 1
            ans += cnt
        elif pre == ')':
            ans += 1
            cnt -= 1
    pre = i
print(ans)