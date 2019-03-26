N = int(input())
F = int(input())
N = (N // 100) * 100
if N % F:
    ans = F - (N % F)
else:
    ans = 0
if ans < 10:
    ans = '0' + str(ans)
print(ans)