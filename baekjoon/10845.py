import sys
st = []
T = int(sys.stdin.readline())
for _ in range(T):
    get = sys.stdin.readline().split()
    if get[0] == 'push':
        st.append(get[1])
    elif get[0] == 'back':
        if st:
            print(st[-1])
        else:
            print(-1)
    elif get[0] == 'front':
        if st:
            print(st[0])
        else:
            print(-1)
    elif get[0] == 'size':
        print(len(st))
    elif get[0] == 'pop':
        if st:
            print(st.pop(0))
        else:
            print(-1)
    elif get[0] == 'empty':
        if st:
            print(0)
        else:
            print(1)