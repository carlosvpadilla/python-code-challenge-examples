#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""Generate all permutations for all numbers from 0 to n."""
from itertools import permutations

class RecursivePermutations:
    permutation: list
    chosen: set

    def _reset(self):
        self.permutation = []
        self.chosen = set()
    
    def __init__(self):
        self._reset()
    
    def _print_recursive_permutations(self, n: int) -> None:
        """Print all permutations of all integers from 0 up to n-1.

        The algorithm basically runs a series of nested for-statements,
        discarding those elements that have been called in previous calls and
        only adding new elements into the permutation.

        Assuming n = 3.

        Call 1:
        * ``permutation = [], len(permutation) == 0``
        * ``chosen = {}``
        * ``len(permutation) == n? False``
        * ``i == 0, i in chosen? False``
        * ``chosen.add(0) == {0}``
        * ``permutation.append(0) == [0]``
        * Call 2 recursive.

        Call 2:
        * ``permutation = [0], len(permutation) == 1``
        * ``chosen = {0}``
        * ``len(permutation) == n? False``
        * ``i == 0, i in chosen? True``
        * ``i == 1, i in chosen? False``
        * ``chosen.add(1) == {0, 1}``
        * ``permutation.append(1) == [0, 1]``
        * Call 3 recursive.

        Call 3:
        * ``permutation = [0, 1], len(permutation) == 2``
        * ``chosen = {0, 1}``
        * ``len(permutation) == n? False``
        * ``i == 0, i in chosen? True``
        * ``i == 1, i in chosen? True``
        * ``i == 2, i in chosen? False``
        * ``chosen.add(2) == {0, 1, 2}``
        * ``permutation.append(2) == [0, 1, 2]``
        * Call 4 recursive.

        Call 4:
        * ``permutation = [0, 1, 2], len(permutation) == 3``
        * ``chosen = {0, 1, 2}``
        * ``len(permutation) == n? True``
        * ``print(permutation)``
        * Return to Call 3.

        Call 3:
        * ``chosen.remove(2) == {0, 1}``
        * ``permutation.pop() == [0, 1]``
        * No more items to iterate, return to Call 2.

        Call 2:
        * ``chosen.remove(1) == {0}``
        * ``permutation.pop() == [0]``
        * ``i == 2, i in chosen? False``
        * ``chosen.add(2) = {0, 2}``
        * ``permutation.append(2) = [0, 2]``
        * Call 5 recursive.

        Call 5:
        * ``permutation = [0, 2], len(permutation) == 2``
        * ``chosen = {0, 2}``
        * ``len(permutation) == n? False``
        * ``i == 0, i in chosen? True``
        * ``i == 1, i in chosen? False``
        * ``chosen.add(1) == {0, 1, 2}``
        * ``permutation.append(1) == [0, 2, 1]``
        * Call 6 recursive.

        Call 6:
        * ``permutation = [0, 2, 1], len(permutation) == 3``
        * ``chosen = {0, 1, 2}``
        * ``len(permutation) == n? True``
        * ``print(permutation)``
        * Return to Call 5.

        Call 5:
        * ``chosen.remove(1) == {0, 2}``
        * ``permutation.pop() == [0, 2]``
        * ``i == 2, i in chosen? True``
        * No more items to iterate, return to Call 2.

        Call 2:
        * ``chosen.remove(2) == {0}``
        * ``permutation.pop() == [0]``
        * No more items to iterate, return to Call 1.
        """
        if len(self.permutation) == n:
            print(self.permutation)
        else:
            for i in range(0, n):
                if i in self.chosen:
                    continue
                self.chosen.add(i)
                self.permutation.append(i)
                self._print_recursive_permutations(n)
                self.chosen.remove(i)
                self.permutation.pop()
        
    def print_recursive_permutations(self, n: int) -> None:
        self._reset()
        self._print_recursive_permutations(n)
    
    def _generate_recursive_permutations(self, n: int) -> list[list]:
        if len(self.permutation) == n:
            return [[i for i in self.permutation]]
        permutations = []
        for i in range(0, n):
            if i in self.chosen:
                continue
            self.chosen.add(i)
            self.permutation.append(i)
            permutations += self._generate_recursive_permutations(n)
            self.chosen.remove(i)
            self.permutation.pop()
        return permutations
    
    def generate_recursive_permutations(self, n: int) -> list[list]:
        self._reset()
        return self._generate_recursive_permutations(n)


def generate_itertools_permutations(n: int) -> list[tuple]:
    return [p for p in permutations(range(n))]


if __name__ == "__main__":
    rp = RecursivePermutations()
    print("We can print all recursive permutations")
    rp.print_recursive_permutations(3)
    print("Or generate a list of all possible permutations")
    print(rp.generate_recursive_permutations(3))
    print("Or just use itertools")
    print(generate_itertools_permutations(3))
