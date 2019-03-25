def sol(value, n):
    global N, min_value, max_value
    if n == N: # 계산이 끝났다면 max, min확인하고 종료
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
        return
    for i in range(4): # +, -, *, / 있는지 확인하고 계산해서 넣고 돌려주고
        if i == 0 and cal[i]:
            cal[i] -= 1
            sol(value + number[n], n + 1)# 계산하면서 넘김
            cal[i] += 1
        elif i == 1 and cal[i]:
            cal[i] -= 1
            sol(value - number[n], n + 1)
            cal[i] += 1
        elif i == 2 and cal[i]:
            cal[i] -= 1
            sol(value * number[n], n + 1)
            cal[i] += 1
        elif i == 3 and cal[i]:
            cal[i] -= 1
            if value < 0:
                sol(-(abs(value)//number[n]), n + 1)
            else:
                sol(value // number[n], n + 1)
            cal[i] += 1

N = int(input())
number = list(map(int, input().split()))
cal = list(map(int, input().split()))
min_value = 2**31
max_value = -min_value
sol(number[0], 1) # 처음 숫자랑 다음 어떤 숫자 쓸지 체크
print(max_value)
print(min_value)