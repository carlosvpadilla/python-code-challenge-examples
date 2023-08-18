#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 
from time import time


def generate_subsets(items: list[int]) -> list[set]:
    b = 0
    subsets = []
    while b < (1 << len(items)):
        subset = set()
        for i in range(0, len(items)):
            if b & 1 << i:
                subset.add(items[i])
        b += 1
        subsets.append(subset)
    return subsets


def check_target_sum_unoptimized(items: list[int], n: int) -> bool:
    subsets = generate_subsets(items)
    for subset in subsets:
        if sum(subset) == n:
            return True
    return False


def check_target_sum_meet_in_middle(items: list[int], n: int) -> bool:
    first_subsets = generate_subsets(items[:len(items)//2])
    first_list = sorted([
        sum(subset)
        for subset in first_subsets
    ])

    second_subsets = generate_subsets(items[len(items)//2:])
    second_list = sorted([
        sum(subset)
        for subset in second_subsets
    ])
    for i in first_list:
        for j in second_list:
            if i + j == n:
                return True
    return False

if __name__ == "__main__":
    input_list = [2, 4, 5, 9]
    target_number = 15
    print("Assume we have this list:")
    print(input_list)
    print("We want to find out if it's possible to add any numbers from that "
          f"list to add up to {target_number}")
    print("We can do a large search in the list. Look how much time it takes.")
    start_time = time()
    print(check_target_sum_unoptimized(input_list, target_number))
    execution_time = time() - start_time
    print(f"That took {execution_time} seconds.")
    print("Now, let's use the meet in the middle technique")
    start_time = time()
    print(check_target_sum_meet_in_middle(input_list, target_number))
    execution_time = time() - start_time
    print(f"That took {execution_time} seconds.")
