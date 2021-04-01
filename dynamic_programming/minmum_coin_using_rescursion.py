# how to make certain change using minimum coins

def get_change(change, availble_coins):
    min_coins = change
    if change in availble_coins:
        return 1
    for coin in [c for c in availble_coins if c <= change]:
        num_of_coins = 1 + get_change(change-coin, availble_coins)
    if num_of_coins<min_coins:
        min_coins = num_of_coins
    return min_coins

print(get_change(13, [1,2,5,10]))