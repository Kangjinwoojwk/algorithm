for tc in range(int(input())):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    state = [0] * (N + 1)
    group = 1
    for i in range(1, N + 1):
        while state[i] == 0:
            state[i] = group
            i = data[i]
            while state[i] == group:
                state[i] = -1
                i = data[i]
        group += 1
    print(len([0 for i in range(1, N + 1) if state[i] > 0]))


# try except까지 썼는데 안되다니...
# for tc in range(int(input())):
#     N = int(input())
#     data = [0] + list(map(int, input().split()))
#     visited = [True] * (N + 1)
#     ans = 0
#     for i in range(1, N + 1):
#         li = list()
#         while visited[i]:
#             visited[i] = False
#             li.append(i)
#             i = data[i]
#             try:
#                 j = li.index(i)
#                 li = li[:j]
#             except ValueError:
#                 continue
#         ans += len(li)
#     print(ans)


# 시간 초과 80%에서 시간 초과가 나온다
# for tc in range(int(input())):
#     N = int(input())
#     data = [0] + list(map(int, input().split()))
#     visited = [True] * (N + 1)
#     ans = 0
#     for i in range(N + 1):
#         if data[i] == i:
#             visited[i] = False
#     for i in range(1, N + 1):
#         if visited[i]:
#             li = list()
#             while visited[i]:
#                 li.append(i)
#                 visited[i] = False
#                 i = data[i]
#                 if i in li:
#                     li = li[:li.index(i)]
#             ans += len(li)
#     print(ans)




