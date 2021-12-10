def solution(money):
    coins = [500, 100, 50, 10]
    coinNo = 0
    for coin in coins:
        coinNo += (money // coin)
        money %= coin
    return coinNo

money = int(input())
result = solution(money)
print(result)