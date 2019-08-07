TimeABC = [300, 60, 10]
ans = [0, 0, 0]
T = int(input())
if T % 10:
    print(-1)
    exit()
for i in range(3):
    ans[i] = T // TimeABC[i]
    T -= (T // TimeABC[i]) * TimeABC[i]
print(ans[0], ans[1], ans[2])
