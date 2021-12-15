def solution(k, arr1, arr2):
    for i in range(k):
        max_arr2 = max(arr2)
        arr2.remove(max_arr2)
        arr1.remove(min(arr1))
        arr1.append(max_arr2)

    result = 0

    for number in arr1:
        result += number

    return result

print(solution(3, [1, 5, 4, 2, 3], [5, 5, 6, 6, 5]))