#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
"""Find the longest increasing subsequence."""
from time import time
import bisect


def nested_loop_solve(input: list[int]) -> int:
    length = dict()
    n = len(input)
    for k in range(n):
        length[k] = 1
        for i in range(k):
            if input[i] < input[k]:
                length[k] = max(length[k], length[i] + 1)
    
    best = 0
    for l in length.values():
        if best < l:
            best = l
    return best


def optimized_solve(input: list[int]) -> int:
    ans = [input[0]]

    for item in input[1:]:
        if item > ans[-1]:
            ans.append(item)
        else:
            low = bisect.bisect_left(ans, item)
            if low < 0:
                low = -(low + 1)
            ans[low] = item
    
    return len(ans)


if __name__ == "__main__":
    sequence = [6, 2, 5, 1, 7, 4, 8, 3]
    print("Suppose we have this sequence")
    print(sequence)
    print("And we want to find the longest increasing subsequence.")
    print("That subsequence is the one sequence of not necessarily adjacent "
          "numbers in the original sequence that is strictly increasing.")
    start_time = time()
    result = nested_loop_solve(sequence)
    duration = time() - start_time
    print(f"The longest subsequence has length {result}")
    print(f"A nested loop solution takes {duration} seconds to complete.")
    print("But we can use binary search to solve this same problem.")
    start_time = time()
    result = optimized_solve(sequence)
    duration = time() - start_time
    print(f"The longest subsequence has length {result}")
    print(f"A binary search solution takes {duration} seconds to complete.")
