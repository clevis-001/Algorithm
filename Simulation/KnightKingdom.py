def solution(point):
    x = ord(point[0])
    y = int(point[1])
    count = 0

    moves = [[-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2]]

    for move in moves:
        if ((96 < x + move[0] <= ord('h')) and (0 < y + move[1] <= 8)):
            count += 1

    answer = count
    return answer

print(solution('c2'))
