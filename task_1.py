import time

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_count[i] = coin

    result = {}
    while amount > 0:
        coin = coin_count[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result


amount_to_give = 113
greedy_start_time = time.time()
greedy_result = find_coins_greedy(amount_to_give)
greedy_duration = time.time() - greedy_start_time

min_coins_start_time = time.time()
min_coins_result = find_min_coins(amount_to_give)
min_coins_duration = time.time() - min_coins_start_time

print("Жадібний алгоритм:", greedy_result)
print("Час виконання жадібного алгоритму:", greedy_duration)
print("Динамічне програмування:", min_coins_result)
print("Час виконання динамічного програмування:", min_coins_duration)

large_amount = 100000
greedy_start_time_large = time.time()
_ = find_coins_greedy(large_amount)
greedy_duration_large = time.time() - greedy_start_time_large

min_coins_start_time_large = time.time()
_ = find_min_coins(large_amount)
min_coins_duration_large = time.time() - min_coins_start_time_large

print("Час виконання жадібного алгоритму для великої суми:", greedy_duration_large)
print("Час виконання динамічного програмування для великої суми:", min_coins_duration_large)
