def solution(cards):
    answer = 0
    player = []
    dealer = []
    while cards:
        player.append(cards.pop(0) if cards[0] <= 10 else (cards.pop(0)//10)*10)
        dealer.append(cards.pop(0) if cards[0] <= 10 else (cards.pop(0)//10)*10)
        player.append(cards.pop(0) if cards[0] <= 10 else (cards.pop(0)//10)*10)
        dealer.append(cards.pop(0) if cards[0] <= 10 else (cards.pop(0)//10)*10)
        if 1 in player and 10 in player:
            if 1 in dealer and 10 in dealer:
                continue
            answer += 3
            player =[]
            dealer =[]
            continue
        if dealer[1] == 1 or dealer[1] >= 7:
            if 1 in player and sum(player) >= 7:
                player.append(10)
            while sum(player) < 17:
                player.append(cards.pop(0) if cards and cards[0] <= 10 else (cards.pop(0)//10)*10)
                if 1 in player and sum(player) >= 7:
                    player.append(10)
        if dealer[1] in (4, 5, 6):
            pass
        if dealer[1] in (2, 3):
            if 1 in player and sum(player) >= 2:
                player.append(10)
            while sum(player) < 12:
                player.append(cards.pop(0) if cards[0] <= 10 else (cards.pop(0)//10)*10)
                if 1 in player and sum(player) >= 2:
                    player.append(10)
        if sum(player) > 21:
            answer -= 2
        if 1 in dealer and sum(dealer) >= 7:
                dealer.append(10)
        while sum(dealer) < 17:
            dealer.append(cards.pop(0) if cards[0] <= 10 else (cards.pop(0)//10)*10)
            if 1 in dealer and sum(dealer) >= 7:
                dealer.append(10)
        if sum(dealer) > 21:
            answer += 2
        if sum(player) > sum(dealer):
            answer += 2
        elif sum(dealer) > sum(player):
            answer -= 2
        player = []
        dealer = []
    return answer

print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))