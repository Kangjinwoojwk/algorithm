for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = 0
    a_get = [5000000, 3000000, 2000000, 500000, 300000, 100000]
    b_get = 5120000
    a_check = 1
    b_check = 1
    if a:
        for i in range(6):
            if a - a_check <= 0:
                ans += a_get[a_check - 1]
                break
            a -= a_check
            a_check += 1
    if b:
        for j in range(5):
            if b - b_check <= 0:
                ans += b_get
                break
            b -= b_check
            b_check *= 2
            b_get /= 2
    print(int(ans))