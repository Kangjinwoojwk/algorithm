for tc in range(int(input())):
    data = list(map(int, input().split()))
    ans_sum = 0
    ans_min = 100
    for i in data:
        if i % 2 == 0:
            ans_sum += i
            if i < ans_min:
                ans_min = i
    print(ans_sum, ans_min)