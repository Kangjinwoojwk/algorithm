for tc in range(int(input())):
    ans = int(input())
    for i in range(int(input())):
        option, price = map(int, input().split())
        ans += option * price
    print(ans)