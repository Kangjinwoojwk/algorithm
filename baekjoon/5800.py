for tc in range(1, int(input()) + 1):
    data = list(map(int, input().split()))
    data = data[1:]
    data.sort()
    lg = 0
    for i in range(1, len(data)):
        if lg < data[i] - data[i - 1]:
            lg = data[i] - data[i - 1]
    print('Class {}'.format(tc))
    print('Max {}, Min {}, Largest gap {}'.format(data[-1], data[0], lg))

# 뭐가 안되지...
# for tc in range(1, int(input()) + 1):
#     data = list(map(int, input().split()))
#     score = [False] * 101
#     minScore = 100
#     maxScore = 0
#     maxGap = 0
#     Gap = -100
#     for i in range(1, data[0] + 1):
#         score[data[i]] = True
#     for i in range(101):
#         if score[i]:
#             if i < minScore:
#                 minScore = i
#             if i > maxScore:
#                 maxScore = i
#             if Gap > maxGap:
#                 maxGap = Gap
#             Gap = 0
#         else:
#             Gap += 1
#     print('Class {}'.format(tc))
#     print('Max {}, Min {}, Largest gap {}'.format(maxScore, minScore, maxGap + 1))