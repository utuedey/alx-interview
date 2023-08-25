#!/usr/bin/python3
"""
0-making_change module
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Determines the fewest number of coins needed
    to meet a given amount total.
    Args:
     - coins (List): list of the values of the coins in your possession
     - total (int): total amount
    Return:
      - coins_count (int): fewest number of coins needed
    """
    if total <= 0:
        return 0
    remainder = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_of_coins = len(coins)

    while remainder > 0:
        if coin_index >= num_of_coins:
            return -1
        if remainder - sorted_coins[coin_index] >= 0:
            remainder -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1
    return coins_count
