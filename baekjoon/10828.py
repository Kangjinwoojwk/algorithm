st = []
T = int(input())
for _ in range(T):
    get = input().split()
    if get[0] == 'push':
        st.append(get[1])
    elif get[0] == 'top':
        if st:
            print(st[-1])
        else:
            print(-1)
    elif get[0] == 'size':
        print(len(st))
    elif get[0] == 'pop':
        if st:
            print(st.pop())
        else:
            print(-1)
    elif get[0] == 'empty':
        if st:
            print(0)
        else:
            print(1)




# 런타임 에러
# st = []
# size = 0
# T = int(input())
# for _ in range(T):
#     get = input().split()
#     if get[0] == 'push':
#         st.append(get[1])
#         size += 1
#     elif get[0] == 'top':
#         print(st[size - 1])
#     elif get[0] == 'empty':
#         if size == 0:
#             print(1)
#         else:
#             print(0)
#     elif get[0] == 'pop':
#         if size > 0:
#             print(st.pop())
#             size -= 1
#         else:
#             print(-1)
#     elif get[0] == 'size':
#         print(size)