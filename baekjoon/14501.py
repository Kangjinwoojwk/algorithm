# 뒤로 가면서 전부 넣는 방법을 생각했는데 연산은 늘어나고~
# 전부 넣다가 마지막까지 넣어서 꼬이고~
# 깔끔하게 다음으로 갈때마다 갱신하게 했다.
N = int(input())
dp = [0 for _ in range(N + 1)]
for i in range(N):
    T, P = map(int, input().split())
    if i + T > N:
        pass
    elif dp[i + T] < dp[i] + P:
        dp[i + T] = dp[i] + P
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]
print(dp[-1])




# 간단한 dp를 구현해봤는데 꼬였다.  잘나오다 마지막 예시가...
# 뒷부분에 넣어 주지 않다 보니 0으로 초기화 된다.
# for i in range(N):
#     T, P = map(int, input().split())
#     if i + T > N:
#         continue
#     else:
#         if dp[i] + P > dp[i+T]:
#             dp[i+T] = dp[i] + P
# print(max(dp))