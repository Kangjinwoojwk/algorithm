import sys
N = int(sys.stdin.readline().rstrip())
ans = 1
for _ in range(N):
    ans += int(sys.stdin.readline().rstrip()) - 1
print(ans)