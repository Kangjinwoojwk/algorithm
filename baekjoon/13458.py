N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = N
for i in range(N):
    A[i] -= B
for i in range(N):
    if A[i] > 0:
        ans += (A[i] + C - 1) // C
print(ans)