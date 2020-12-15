# 그리디 알고리즘
# 동전으로 거슬러 줄 수 있는 최소 갯 수 구하기
n = 1540
count = 0

coins = [500, 100, 50, 10]
for coin in coins:
    count += n // coin
    n %= coin

print(count)

# n = 1260
# count = 0
#
# coin_types = [500, 100, 50, 10]
#
# for coin in coin_types:
#     count += n // coin  ## // === 몫
#     n %= coin
#
# print(count)
