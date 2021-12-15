n = int(input())
array = []
for i in range(n):
    number = int(input())
    array.append(number)
array.sort(reverse=True)
for number in array:
    print(number, end = ' ')