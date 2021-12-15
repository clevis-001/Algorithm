array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    current_index = i
    while(current_index >= 1):
        if (array[current_index] >= array[current_index -1]):
            break
        array[current_index], array[current_index -1] = array[current_index -1], array[current_index]
        current_index -= 1
    print(array)


