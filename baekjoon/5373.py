def rotate(a):
    location = a[0]
    direction = a[1]
    if direction == '+':
        cube[location][0][2], cube[location][2][2], cube[location][2][0], cube[location][0][0] = cube[location][0][0], cube[location][0][2], cube[location][2][2], cube[location][2][0]
        cube[location][1][2], cube[location][2][1], cube[location][1][0], cube[location][0][1] = cube[location][0][1], cube[location][1][2], cube[location][2][1], cube[location][1][0]
    else:
        cube[location][0][0], cube[location][0][2], cube[location][2][2], cube[location][2][0] = cube[location][0][2], cube[location][2][2], cube[location][2][0], cube[location][0][0]
        cube[location][0][1], cube[location][1][2], cube[location][2][1], cube[location][1][0] = cube[location][1][2], cube[location][2][1], cube[location][1][0], cube[location][0][1]
        

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
