#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""Calculate number of editions needed to turn one word into another."""


def levenshtein(x: str, y: str) -> int:
    if len(y) == 0:
        return len(x)
    
    if len(x) == 0:
        return len(y)
    
    if x == y:
        return 0
    
    distance = [
        [0 for _ in range(len(x) + 1)]
        for _ in range(len(y) + 1)
    ]

    distance[0] = [
        i for i in range(len(x) + 1)
    ]

    for j in range(1, len(y) + 1):
        b = y[j - 1]
        for i in range(len(x) + 1):
            if i == 0:
                distance[j][i] = j
                continue
            a = x[i - 1]
            cost = 0 if a == b else 1
            distance[j][i] = min(
                distance[j][i-1] + 1,
                distance[j-1][i] + 1,
                distance[j-1][i-1] + cost
            )
    
    return distance[-1][-1]


if __name__ == "__main__":
    x = "love"
    y = "movie"
    print(f"Suppose we have two words: {x} and {y}. "
          "What is the edit distance between both?")
    print(levenshtein(x, y))
    x = "hello"
    y = "goodbye"
    print(f"What about words {x} and {y}?")
    print(levenshtein(x, y))
