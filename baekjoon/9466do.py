for tc in range(int(input())):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [True] * (N + 1)
    li = list()
    for i in range(N + 1):
        if data[i] == i:
            visited[i] = False
    for i in range(1, N + 1):
        check = 0
        while visited[i]:
            li.append(i)
            check += 1
            visited[i] = False
            i = data[i]
            if i in li:
                li = li[:li.index(i)]
    print(len(li))


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




