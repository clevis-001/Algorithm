n = int(input())
votes = []
for i in range(n):
    can1, can2, can3 = map(int, input().split())
    single_vote = [can1, can2, can3]
    votes.append(single_vote)

sum1 = 0
sum2 = 0
sum3 = 0

for i in range(n):
    sum1 += votes[i][0]
    sum2 += votes[i][1]
    sum3 += votes[i][2]

result = [sum1, sum2, sum3]
max_votes = max(result)
answer = 0

if result.count(max_votes) == 3:
    answer = 0

if result.count(max_votes) == 2:
    count3_1 = count()