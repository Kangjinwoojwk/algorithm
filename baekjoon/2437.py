# 1을 만들려면 1 필요, 2만들려면 1 둘 또는 2 필요 근데 2만 있으면 이미 1에서 끝
# 3까지 가려면 1, 2 모두 필요하다 4가려면 1 넷, 1 둘 2 하나 혹은 1과 2 둘, 1과 2와 3, 1,2,4가 있어야 한다.
# 5가려면 4까지 있던 것들만드로 충분하다. 단 1만 4개인 경우 불가, 작은 것들 하나씩 더한 합보다 2이상 크면 못만든다.
N = int(input())
choo = list(map(int, input().split()))
choo.sort()
ans = 0
i = 0
while i < N:
    if ans + 1 < choo[i]:
        break
    ans += choo[i]
    i += 1
ans += 1
print(ans)


# 런타임 에러...어디서 잘못된 것일까...
# 어쩌면 브루트 포스가 문제일지도 모르겠다.
# from collections import deque
# N = int(input())
# choo = list(map(int, input().split()))
# choo.sort()
# weight = [True] * choo[-1] * N
# Q = deque()
# Q.append(0)
# weight[0] = False
# n = 0
# while n < N:
#     for _ in range(len(Q)):
#         temp = Q.popleft()
#         Q.append(temp)
#         temp += choo[n]
#         if weight[temp]:
#             weight[temp] = False
#             Q.append(temp)
#     n += 1
# n = 0
# while n < 1000000000:
#     if weight[n]:
#         print(n)
#         break
#     n += 1