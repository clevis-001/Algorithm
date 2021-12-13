n = int(input())
classnum = [0] * 23
calls = list(map(int, input().split()))
for call in calls:
    classnum[call - 1] += 1

classnum.reverse()

print(classnum)