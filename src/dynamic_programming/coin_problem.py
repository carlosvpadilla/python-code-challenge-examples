#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""How many coins do we need to form a specific sum of money?

Dynamic programming version.
"""


class CoinSolver:
    coins: list[int]
    solutions: dict[int, int]
    first_coins: dict[int, int]
    first_coin: int
    count: dict[int, int]


    def __init__(self, coins: list[int]) -> None:
        self.coins = coins
        self.solutions = {0: 0}
        self.first_coins = dict()
        self.first_coin = 0
        self.count = {0: 1}

    def solve(self, n: int) -> int:
        for x in range(1, n+1):
            self.solutions[x] = None
            self.count[x] = 0
            for c in self.coins:
                if x - c >= 0:
                    self.count[x] += self.count[x-c]
                    if (self.solutions[x] is None
                            or self.solutions[x-c] + 1 < self.solutions[x]):
                        self.solutions[x] = self.solutions[x-c] + 1
                        self.first_coins[x] = c
        self.first_coin = self.first_coins[n]
        return self.solutions[n]


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    n = 520
    solver_euros = CoinSolver(coins)
    print("Assume we have all euro coins available to us, in cents")
    print(coins)
    print(f"How many coins do we need to get {n} cents?")
    print(solver_euros.solve(n))
    coins = [1, 3, 4]
    n = 6
    solver_general = CoinSolver(coins)
    print("Unlike the greedy case, we can generalize this dynamic approach. "
          "Assume these coins:")
    print(coins)
    print(f"The target is {n}. The optimal solution is 2 coins, 3+3.")
    solution = solver_general.solve(n)
    print(solution)
    print("And now we have a general solution.")
    print("This way we can even see what's the first coin of any given solution:")
    print(solver_general.first_coin)
    print("And these are all the coins in the solution:")
    n_coins = n
    all_coins = []
    while n_coins > 0:
        coin = solver_general.first_coins[n_coins]
        all_coins.append(str(coin))
        n_coins -= coin
    print("+".join(all_coins))
    print(f"And there are this many solutions for this problem: {solver_general.count[n]}")
