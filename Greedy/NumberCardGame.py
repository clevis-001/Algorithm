n, m = map(int, input().split())
minArray = []

for _ in range(n):
    array = list(map(int, input().split()))
    minArray.append(min(array))

print(max(minArray))