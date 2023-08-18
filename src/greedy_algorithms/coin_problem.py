#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""For a sum of money considering certain coins."""


def greedy_coins(coins: list, n: int) -> int:
    # Ensure that the list is sorted in a descending manner
    sorted_coins = sorted(coins, reverse=True)
    total = 0
    number_of_coins = 0
    while total < n:
        for coin in sorted_coins:
            if total + coin > n:
                continue
            total += coin
            number_of_coins += 1
            break
    return number_of_coins if total == n else -1


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    n = 520
    print("Assume we have all euro coins available to us, in cents")
    print(coins)
    print(f"How many coins do we need to get {n} cents?")
    print(greedy_coins(coins, n))
    coins = [1, 3, 4]
    n = 6
    print("But this does not work for the general case. Assume these coins:")
    print(coins)
    print(f"The target is {n}. The optimal solution is 2 = 3+3.")
    print("But the code says...")
    print(greedy_coins(coins, n))
    print("This algorithm does not generalize well, although it works for "
          "euros.")
    print("See dynamic programming for a different approach.")