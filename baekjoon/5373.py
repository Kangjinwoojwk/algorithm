def rotate(a):
    location = a[0]
    direction = a[1]
    if direction == '+':
        cube[location][0][2], cube[location][2][2], cube[location][2][0], cube[location][0][0] = cube[location][0][0], cube[location][0][2], cube[location][2][2], cube[location][2][0]
        cube[location][1][2], cube[location][2][1], cube[location][1][0], cube[location][0][1] = cube[location][0][1], cube[location][1][2], cube[location][2][1], cube[location][1][0]
    else:
        cube[location][0][0], cube[location][0][2], cube[location][2][2], cube[location][2][0] = cube[location][0][2], cube[location][2][2], cube[location][2][0], cube[location][0][0]
        cube[location][0][1], cube[location][1][2], cube[location][2][1], cube[location][1][0] = cube[location][1][2], cube[location][2][1], cube[location][1][0], cube[location][0][1]
    if a == 'U+':
        cube['F'][0][0], cube['F'][0][1], cube['F'][0][2], cube['R'][0][0], cube['R'][0][1], cube['R'][0][2], \
        cube['B'][0][0], cube['B'][0][1], cube['B'][0][2], cube['L'][0][0], cube['L'][0][1], cube['L'][0][2] = \
        cube['L'][0][0], cube['L'][0][1], cube['L'][0][2], cube['F'][0][0], cube['F'][0][1], cube['F'][0][2], \
        cube['R'][0][0], cube['R'][0][1], cube['R'][0][2], cube['B'][0][0], cube['B'][0][1], cube['B'][0][2]
    elif a == 'U-':
        cube['L'][0][0], cube['L'][0][1], cube['L'][0][2], cube['F'][0][0], cube['F'][0][1], cube['F'][0][2], \
        cube['R'][0][0], cube['R'][0][1], cube['R'][0][2], cube['B'][0][0], cube['B'][0][1], cube['B'][0][2] = \
        cube['F'][0][0], cube['F'][0][1], cube['F'][0][2], cube['R'][0][0], cube['R'][0][1], cube['R'][0][2], \
        cube['B'][0][0], cube['B'][0][1], cube['B'][0][2], cube['L'][0][0], cube['L'][0][1], cube['L'][0][2]
    elif a == 'D+':
        cube['F'][2][0], cube['F'][2][1], cube['F'][2][2], cube['R'][2][0], cube['R'][2][1], cube['R'][2][2], \
        cube['B'][2][0], cube['B'][2][1], cube['B'][2][2], cube['L'][2][0], cube['L'][2][1], cube['L'][2][2] = \
        cube['L'][2][0], cube['L'][2][1], cube['L'][2][2], cube['F'][2][0], cube['F'][2][1], cube['F'][2][2], \
        cube['R'][2][0], cube['R'][2][1], cube['R'][2][2], cube['B'][2][0], cube['B'][2][1], cube['B'][2][2]
    elif a == 'D-':
        cube['L'][2][0], cube['L'][2][1], cube['L'][2][2], cube['F'][2][0], cube['F'][2][1], cube['F'][2][2], \
        cube['R'][2][0], cube['R'][2][1], cube['R'][2][2], cube['B'][2][0], cube['B'][2][1], cube['B'][2][2] = \
        cube['F'][2][0], cube['F'][2][1], cube['F'][2][2], cube['R'][2][0], cube['R'][2][1], cube['R'][2][2], \
        cube['B'][2][0], cube['B'][2][1], cube['B'][2][2], cube['L'][2][0], cube['L'][2][1], cube['L'][2][2]
    elif a == 'L+':
        cube['F'][0][0], cube['F'][1][0], cube['F'][2][0], cube['D'][0][0], cube['D'][1][0], cube['D'][2][0], \
        cube['B'][0][2], cube['B'][1][2], cube['B'][2][2], cube['U'][0][0], cube['U'][1][0], cube['U'][2][0] = \
        cube['U'][0][0], cube['U'][1][0], cube['U'][2][0], cube['F'][0][0], cube['F'][1][0], cube['F'][2][0], \
        cube['D'][2][0], cube['D'][1][0], cube['D'][0][0], cube['B'][2][2], cube['B'][1][2], cube['B'][0][2]
    elif a == 'L-':
        cube['U'][0][0], cube['U'][1][0], cube['U'][2][0], cube['F'][0][0], cube['F'][1][0], cube['F'][2][0], \
        cube['D'][0][0], cube['D'][1][0], cube['D'][2][0], cube['B'][2][2], cube['B'][2][1], cube['B'][2][0] = \
        cube['F'][0][0], cube['F'][1][0], cube['F'][2][0], cube['D'][0][0], cube['D'][1][0], cube['D'][2][0], \
        cube['B'][2][2], cube['B'][1][2], cube['B'][0][2], cube['U'][0][0], cube['U'][0][1], cube['U'][0][2]
    elif a == 'R+':
        cube['U'][0][2], cube['U'][1][2], cube['U'][2][2], cube['F'][0][2], cube['F'][1][2], cube['F'][2][2], \
        cube['D'][0][2], cube['D'][1][2], cube['D'][2][2], cube['B'][0][0], cube['B'][0][1], cube['B'][0][2] = \
        cube['F'][0][2], cube['F'][1][2], cube['F'][2][2], cube['D'][0][2], cube['D'][1][2], cube['D'][2][2], \
        cube['B'][2][0], cube['B'][1][0], cube['B'][0][0], cube['U'][2][2], cube['U'][2][1], cube['U'][2][0]
    elif a == 'R-':
        cube['F'][0][2], cube['F'][1][2], cube['F'][2][2], cube['D'][0][2], cube['D'][1][2], cube['D'][2][2], \
        cube['B'][2][0], cube['B'][1][0], cube['B'][0][0], cube['U'][2][2], cube['U'][2][1], cube['U'][2][0] = \
        cube['U'][0][2], cube['U'][1][2], cube['U'][2][2], cube['F'][0][2], cube['F'][1][2], cube['F'][2][2], \
        cube['D'][0][2], cube['D'][1][2], cube['D'][2][2], cube['B'][0][0], cube['B'][0][1], cube['B'][0][2]
    elif a == 'F+':
        cube['U'][2][0], cube['U'][2][1], cube['U'][2][2], cube['R'][0][0], cube['R'][1][0], cube['R'][2][0], \
        cube['D'][0][2], cube['D'][0][1], cube['D'][0][0], cube['L'][2][2], cube['L'][1][2], cube['L'][0][2] = \
        cube['L'][2][2], cube['L'][1][2], cube['L'][0][2], cube['U'][2][0], cube['U'][2][1], cube['U'][2][2], \
        cube['R'][0][0], cube['R'][1][0], cube['R'][2][0], cube['D'][0][2], cube['D'][0][1], cube['D'][0][0]
    elif a == 'F-':
        cube['L'][2][2], cube['L'][1][2], cube['L'][0][2], cube['U'][2][0], cube['U'][2][1], cube['U'][2][2], \
        cube['R'][0][0], cube['R'][1][0], cube['R'][2][0], cube['D'][0][2], cube['D'][0][1], cube['D'][0][0] = \
        cube['U'][2][0], cube['U'][2][1], cube['U'][2][2], cube['R'][0][0], cube['R'][1][0], cube['R'][2][0], \
        cube['D'][0][2], cube['D'][0][1], cube['D'][0][0], cube['L'][2][2], cube['L'][1][2], cube['L'][0][2]
    elif a == 'B+':
        cube['L'][2][0], cube['L'][1][0], cube['L'][0][0], cube['U'][0][0], cube['U'][0][1], cube['U'][0][2], \
        cube['R'][0][2], cube['R'][1][2], cube['R'][2][2], cube['D'][2][2], cube['D'][2][1], cube['D'][2][0] = \
        cube['U'][0][0], cube['U'][0][1], cube['U'][0][2], cube['R'][0][2], cube['R'][1][2], cube['R'][2][2], \
        cube['D'][2][2], cube['D'][2][1], cube['D'][2][0], cube['L'][2][0], cube['L'][1][0], cube['L'][0][0]
    elif a == 'B-':
        cube['U'][0][0], cube['U'][0][1], cube['U'][0][2], cube['R'][0][2], cube['R'][1][2], cube['R'][2][2], \
        cube['D'][2][2], cube['D'][2][1], cube['D'][2][0], cube['L'][2][0], cube['L'][1][0], cube['L'][0][0] = \
        cube['L'][2][0], cube['L'][1][0], cube['L'][0][0], cube['U'][0][0], cube['U'][0][1], cube['U'][0][2], \
        cube['R'][0][2], cube['R'][1][2], cube['R'][2][2], cube['D'][2][2], cube['D'][2][1], cube['D'][2][0]


for tc in range(int(input())):
    cube = {
        'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
        'D': [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
        'F': [['r', 'r', 'r'], ['r', 'r', 'r'],['r', 'r', 'r']],
        'B': [['o', 'o', 'o'], ['o', 'o', 'o'],['o', 'o', 'o']],
        'L': [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        'R': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]}
    n = int(input())
    data = input().split()
    for i in data:
        rotate(i)
    for i in cube['U']:
        print(''.join(i))
