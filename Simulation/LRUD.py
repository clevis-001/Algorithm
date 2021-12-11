def solution(size, moves):
    move_types = dict()

    move_types['L'] = [0, -1]
    move_types['R'] = [0, 1]
    move_types['U'] = [-1, 0]
    move_types['D'] = [1, 0]

    x = 1
    y = 1

    for move in moves:
        x += move_types[move][0]
        y += move_types[move][1]

        if ((x <= 0 or x > size) or (y <= 0 or y > size)):
            x -= move_types[move][0]
            y -= move_types[move][1]

    answer = [x, y]
    return answer


print(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']))
