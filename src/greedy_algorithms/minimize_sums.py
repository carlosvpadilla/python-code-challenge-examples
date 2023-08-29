#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""Find x that minimizes the sum"""
from abc import ABC
from abc import abstractmethod
from statistics import median_low
from statistics import mean


class Polynomial(ABC):
    terms: list[int]
    c: int

    def __init__(self, c: int, *args):
        self.terms = [arg for arg in args]
        self.c = c

    def verify(self, x: int) -> int:
        sum = 0
        for term in self.terms:
            sum += pow(term - x, self.c)
        return sum
    
    @abstractmethod
    def solve(self) -> float:
        ...


class C1Polynomial(Polynomial):
    def __init__(self, *args):
        super().__init__(1, *args)

    def solve(self) -> float:
        return median_low(self.terms)
    
    def __str__(self) -> str:
        str_terms = []
        for term in self.terms:
            str_terms.append(f"|{term} - x|")
        return " + ".join(str_terms)


class C2Polynomial(Polynomial):
    def __init__(self, *args):
        super().__init__(2, *args)

    def solve(self) -> float:
        return mean(self.terms)
    
    def __str__(self) -> str:
        str_terms = []
        for term in self.terms:
            str_terms.append(f"({term} - x)^2")
        return " + ".join(str_terms)
    

if __name__ == "__main__":
    c1_polynomial = C1Polynomial(1, 2, 9, 2, 6)
    print("Let us suppose we have this sum:")
    print(c1_polynomial)
    print("We want to select some x that minimizes this sum.")
    print("We select the median of this polynomial, which yields this value:")
    c1_result = c1_polynomial.solve()
    print(c1_result)
    print(f"And using that median, the minimum sum is {c1_polynomial.verify(c1_result)}")
    c2_polynomial = C2Polynomial(1, 2, 9, 2, 6)
    print("What if we squared the terms like this?")
    print(c2_polynomial)
    print("Instead we want to take the average of the terms:")
    c2_result = c2_polynomial.solve()
    print(c2_result)
    print(f"Which yields the value {c2_polynomial.verify(c2_result)}")
