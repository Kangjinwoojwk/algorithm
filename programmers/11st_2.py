def solution(balloons):
    positiveX = negativeX = positiveY = negativeY = False
    for i in balloons:
        if i[1] == 0:
            if i[0] < 0:
                negativeX = True
            if i[0] > 0:
                positiveX = True
        elif i[0] == 0:
            if i[1] < 0:
                negativeY = True
            if i[1] > 0:
                positiveY = True
    ans1 = set([i[0]/i[1] for i in balloons if i[0] > 0 and i[1] > 0])
    ans2 = set([i[0]/i[1] for i in balloons if i[0] < 0 and i[1] > 0])
    ans3 = set([i[0]/i[1] for i in balloons if i[0] < 0 and i[1] < 0])
    ans4 = set([i[0]/i[1] for i in balloons if i[0] > 0 and i[1] < 0])
    answer = len(ans1) + len(ans2) + len(ans3) + len(ans4) + positiveX + negativeX + positiveY + negativeY
    return answer

# SELECT ID, TITLE, CHANNEL_TITLE
# FROM YOUTUBES
# WHERE CHANNEL_TITLE LIKE '%VEVO'
# ORDER BY ID;

# SELECT ID
# FROM GAME_USERS
# WHERE IDNOT IN (SELECT ID1 FROM FRIENDS) AND ID NOT IN (SELECT ID2 FROM FRIENDS);