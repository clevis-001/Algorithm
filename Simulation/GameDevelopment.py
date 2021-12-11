def solution(positon, map_info):
    loc_x, loc_y, dir_key = map(int, positon)
    direction = dict()
    direction[0] = [0, -1]
    direction[1] = [1, 0]
    direction[2] = [0, 1]
    direction[3] = [-1, 0]
    count = 1

    map_info[loc_x][loc_y] = -1

    while(True):
        turns = [0, 0, 0, 0]
        for i in range(4):
            dir_key -= 1
            if (dir_key == -1) : dir_key += 4
            move_x = direction[dir_key][0] + loc_x
            move_y = direction[dir_key][1] + loc_y
            print(move_x, move_y)
            if (map_info[move_x][move_y] == 0) :
                loc_x = move_x
                loc_y = move_y
                map_info[loc_x][loc_y] = -1
                print(map_info)
                count += 1
                break
            if (map_info[move_x][move_y] == 1 or map_info[move_x][move_y] == -1):
                turns[i] = -1
        if (turns == [-1, -1, -1, -1]):
            loc_x -= direction[dir_key][0]
            loc_y -= direction[dir_key][1]
            if (map_info[loc_x][loc_y] == 1):
                break

    answer = count
    return answer

print(solution([1, 1, 0], [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,0,1],[1,1,1,1]]))







