N = int(input())
ans = 0
for i in range(N):
    ans += int(input())
if ans > N//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')