for_sort = [3, 7, 6, 5, 1, 2, 8, 4, 9, 0]

def quick_sort(for_sort):

    if len(for_sort) == 1:
        return for_sort

    pivot = for_sort[0]

    big_index = 1
    small_index = len(for_sort) - 1

    while small_index > big_index:

        while for_sort[big_index] < pivot:
            big_index += 1

        while for_sort[small_index] > pivot:
            small_index -= 1

        for_sort[big_index], for_sort[small_index] = for_sort[small_index], for_sort[big_index]

        print(for_sort)

    for_sort[0], for_sort[small_index] = for_sort[small_index], for_sort[0]
    print(for_sort)

    quick_sort(for_sort[:small_index])
    quick_sort(for_sort[small_index + 1:])


print(quick_sort(for_sort))

