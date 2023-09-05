#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""Solving knapsack problems."""


def determine_all_sums(w: list[int]) -> list[int]:
    max_sum = sum(w)
    possible = [
        [False for _ in range(max_sum + 1)]
        for _ in range(len(w) + 1)
    ]

    possible[0][0] = True

    for k in range(len(w) + 1):
        for x in range(max_sum + 1):
            if k == 0:
                possible[k][x] = (x == 0)
                continue
            if x - w[k-1] >= 0:
                possible[k][x] = possible[k][x] or possible[k-1][x - w[k-1]]
            possible[k][x] = possible[k][x] or possible[k-1][x]

    return [
        i for i, j in enumerate(possible[-1])
        if j is True
    ]


def optimum_all_sums(w: list[int]) -> list[int]:
    max_sum = sum(w)
    possible = [
        False for _ in range(max_sum + 1)
    ]

    possible[0] = True

    for k in range(1, len(w) + 1):
        for x in range(max_sum, -1, -1):
            if possible[x]:
                possible[x + w[k-1]] = True
    
    return [
        i for i, j in enumerate(possible)
        if j is True
    ]


if __name__ == "__main__":
    weights = [1, 3, 3, 5]
    print("Suppose we have the following weights, in order")
    print(weights)
    print("We want to know what sums we can build with this set of numbers")
    print("This is known as a knapsack problem. Let's see the solution:")
    print(determine_all_sums(weights))
    print("We need to store all sums as we go through them.")
    print("This algorithm is more optimal, however")
    print(optimum_all_sums(weights))
