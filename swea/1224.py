import sys
sys.stdin = open('1224.txt')
sys.stdout = open('1224_out.txt', 'w')
for test_case in range(1, 11):
    N = int(input())
    st = []
    st_top = -1
    sub_st = []
    sub_st_top = -1
    for i in input():
        if i == '(':
            N -= 1
            sub_st.append(i)
            sub_st_top += 1
        elif i == ')':
            N -= 1
            while sub_st[sub_st_top] != '(':
                st.append(sub_st[sub_st_top])
                sub_st = sub_st[:-1]
                sub_st_top -= 1
            sub_st = sub_st[:-1]
            sub_st_top -= 1
        elif i == '+':
            if sub_st_top != -1 and (sub_st[sub_st_top] == '*' or sub_st[sub_st_top] == '+'):
                st.append(sub_st[sub_st_top])
                sub_st = sub_st[:-1]
                sub_st_top -= 1
                st_top += 1
            sub_st.append(i)
            sub_st_top += 1
        elif i == '*':
            if sub_st_top != -1 and sub_st[sub_st_top] == '*':
                st.append(sub_st[sub_st_top])
                sub_st = sub_st[:-1]
                sub_st_top -= 1
                st_top += 1
            sub_st.append(i)
            sub_st_top += 1
        else:
            st.append(i)
            st_top += 1
    else:
        while sub_st_top != -1:
            st.append(sub_st[sub_st_top])
            sub_st_top -= 1
    ptr = 0
    while len(st) != 1:
        if st[ptr] == '+':
            st[ptr - 2] = str(int(st[ptr - 2]) + int(st[ptr - 1]))
            st = st[:ptr - 1] + st[ptr + 1:]
            ptr -= 2
        elif st[ptr] == '*':
            st[ptr - 2] = str(int(st[ptr - 2]) * int(st[ptr - 1]))
            st = st[:ptr - 1] + st[ptr + 1:]
            ptr -= 2
        else:
            ptr += 1
    print('#{} {}'.format(test_case, st[0]))
