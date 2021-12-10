n, m, k = map(int, input().split())
data = list(map(int, input().split()))

def solution(n, m, k, data):
    data.sort()
    no = m // (k+1)
    noLeft = m % (k+1)
    sum = ((k * no) + noLeft) * data[-1] + (no * data[-2])
    return sum

print(solution(n, m ,k, data))