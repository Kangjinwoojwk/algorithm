# 버튼을 누르는 손가락은?

def solution(numbers, hand):
    answer = ''
    location = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)
                }
    left = (3, 0)
    right = (3, 2)
    for i in numbers:
        if location[i][1] == 0:
            answer += 'L'
            left = location[i]
        elif location[i][1] == 2:
            answer += 'R'
            right = location[i]
        else:
            ldistance = abs(left[0] - location[i][0]) + abs(left[1] - location[i][1])
            rdistance = abs(right[0] - location[i][0]) + abs(right[1] - location[i][1])
            if ldistance < rdistance:
                answer += 'L'
                left = location[i]
            elif ldistance > rdistance:
                answer += 'R'
                right = location[i]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = location[i]
                elif hand == 'right':
                    answer += 'R'
                    right = location[i]

    return answer