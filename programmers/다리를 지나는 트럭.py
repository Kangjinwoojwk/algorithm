def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    bridge_weight = 0
    while truck_weights or bridge:
        answer += 1
        if bridge and bridge[0][1] + bridge_length == answer:
            bridge_weight -= bridge[0][0]
            bridge.pop(0)
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            bridge.append([truck_weights[0], answer])
            bridge_weight += truck_weights[0]
            truck_weights.pop(0)

    return answer


# 시뮬레이션, 시간초과
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0] * bridge_length
#     bridge_weight = 0
#     while truck_weights or bridge_weight:
#         answer += 1
#         bridge_weight -= bridge[0]
#         for i in range(bridge_length - 1):
#             bridge[i] = bridge[i + 1]
#         if truck_weights and bridge_weight + truck_weights[0] <= weight:
#             bridge[-1] = truck_weights[0]
#             bridge_weight += truck_weights[0]
#             truck_weights.pop(0)
#         else:
#             bridge[-1] = 0
#     return answer