import time 

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        result[coin] = amount // coin
        amount %= coin
    return result

def find_min_coins(amount):
    min_coins = [0] + [float('inf')] * amount
    used_coin = [{} for _ in range(amount + 1)]

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coin[i] = used_coin[i - coin].copy()
                used_coin[i][coin] = used_coin[i].get(coin, 0) + 1

    return used_coin[amount]



# Тesting the result for 113
amount = 113

# Greedy algorithm
start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

# Dymanic programming
start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time


print(f"Жадібний алгоритм: {greedy_result}, Час виконання: {greedy_time:.6f} c.")
print(f"Динамічне програмування: {dp_result}, Час виконання: {dp_time:.6f} c.")