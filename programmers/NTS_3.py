def solution(input):
    answer = True
    OP = ['(', '{', '[']
    ED = [')', '}', ']']
    st = list()
    for i in input:
        if i in OP:
            if (not st or OP.index(i) < OP.index(st[-1])):
                st.append(i)
            else:
                return False
        elif i in ED:
            if st and ED.index(i) == OP.index(st[-1]):
                st.pop()
            else:
                return False
    if st:
        return False
    return answer

print(solution('3+[(5+1)-1]'))