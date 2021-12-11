def solution(n):
    count = 0
    for x in range(0, n+1):
        str_x = str(x)
        for y in range(0, 60):
            str_y = str(y)
            for z in range(0, 60):
                str_z = str(z)
                time = str_x + '시' + str_y + '분' + str_z + '초'
                if '3' in time:
                    count += 1

    answer = count
    return answer

print(solution(5))
