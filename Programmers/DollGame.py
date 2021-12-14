def solution(board, moves):
    result = 0
    box = []
    for move in moves:
        for i in range(len(board)):
            if (board[i][move -1] != 0):
                pick = board[i][move -1]
                board[i][move -1] = 0
                box.append(pick)
                if (len(box) >= 2 and box[-1] == box[-2]):
                    box.pop()
                    box.pop()
                    result += 2
                break
    return result


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))