#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""Find the maximum sum path in a grid."""
from typing import Optional
import random


class MaxSumGrid:
    values: list[list[int]]
    n: int

    def __init__(self, n: int, values: Optional[list[list[int]]] = None) -> None:
        self.n = n
        if values is not None:
            if len(values) != n:
                raise ValueError(f"The number of rows must be {n}")
            for row in values:
                if len(row) != n:
                    raise ValueError(f"The number of columns must be {n}")
            self.values = values
        else:
            self.values = list()
            for i in range(n):
                self.values.append(list())
                for _ in range(n):
                    self.values[i].append(random.randint(1, 10))
    

    def get_max_sum(self) -> int:
        sum_values = {
            i: {
                j: 0
                for j in range(self.n)
            }
            for i in range(self.n)
        }
        for i in range(self.n):
            if i - 1 < 0:
                sum_values[0][i] = self.values[0][i]
                sum_values[i][0] = self.values[i][0]
            else:
                sum_values[0][i] = sum_values[0][i-1] + self.values[0][i]
                sum_values[i][0] = sum_values[i-1][0] + self.values[i][0]
        for i in range(1, self.n):
            for j in range(1, self.n):
                sum_values[i][j] = max(sum_values[i-1][j], sum_values[i][j-1]) + self.values[i][j]
        return sum_values[self.n - 1][self.n - 1]


def print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        print(row)


if __name__ == "__main__":
    print("Assume we have the following grid:")
    grid_mtrx = [
        [3, 7, 9, 2, 7],
        [9, 8, 3, 5, 5],
        [1, 7, 9, 8, 5],
        [3, 8, 6, 4, 10],
        [6, 3, 9, 7, 8]
    ]
    print_grid(grid_mtrx)
    print("If moving down or right, find the path from the top left corner to "
          "the bottom right corner that has the maximum sum")
    grid = MaxSumGrid(5, grid_mtrx)
    print(f"The maximum sum is {grid.get_max_sum()}")
    print("What if we tried a random grid?")
    rndm_grid = MaxSumGrid(5)
    print_grid(rndm_grid.values)
    print(f"Its maximum sum is {rndm_grid.get_max_sum()}")
