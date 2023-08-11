#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 
"""Generate all subsets.

For example, the subsets of ``{0,1,2}`` are ``{}, {0}, {1}, {2}, {0,1},
{0,2}, {1,2}, {0,1,2}``. Two methods exist to explore all subsets: use
recursion, or use the bitwise representation.

Consider that these will generate all subsets for all natural numbers
including zero of size n.
"""

class RecursiveSearch():
    subset: set

    def __init__(self):
        self._reset()

    def _reset(self):
        self.subset = set()
    
    def _print_recursive_search(self, n: int, k: int) -> None:
        if k == n:
            print(self.subset)
        else:
            self._print_recursive_search(n, k+1)
            self.subset.add(k)
            self._print_recursive_search(n, k+1)
            self.subset.remove(k)

    def print_recursive_search(self, n: int) -> None:
        self._reset()
        self._print_recursive_search(n, 0)

    def _generate_recursive_search(self, n: int, k: int) -> list[list]:
        if k == n:
            # If we don't do a copy, which takes O(n), the remove function will
            # remove numbers from the solution
            return [self.subset.copy()]
        else:
            left_search = self._generate_recursive_search(n, k+1)
            self.subset.add(k)
            right_search = self._generate_recursive_search(n, k+1)
            self.subset.remove(k)
            return left_search + right_search
    
    def generate_recursive_search(self, n: int) -> list[list]:
        self._reset()
        return self._generate_recursive_search(n, 0)


def print_bitwise_search(n: int) -> None:
    b = 0
    while b < (1 << n):
        subset = []
        for i in range(0, n):
            if b & 1 << i:
                subset.append(i)
        b += 1
        print(subset)


def generate_bitwise_search(n: int) -> list[set]:
    b = 0
    subsets = []
    while b < (1 << n):
        subset = set()
        for i in range(0, n):
            if b & 1 << i:
                subset.add(i)
        b += 1
        subsets.append(subset)
    return subsets


if __name__ == "__main__":
    rs = RecursiveSearch()
    print("First, print all generated subsets in the function")
    rs.print_recursive_search(3)
    print("Then, generate an array of subsets and print everything")
    print(rs.generate_recursive_search(3))
    print("But we can do the same with bits")
    print_bitwise_search(3)
    print("And we can get a useful list too")
    print(generate_bitwise_search(3))
