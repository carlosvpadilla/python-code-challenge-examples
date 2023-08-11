from itertools import permutations


def print_recursive_permutations(
        n: int, permutation: list=[], chosen: set=set()) -> None:
    """Print all permutations of all integers from 0 up to n-1.

    The algorithm basically runs a series of nested for-statements, discarding
    those elements that have been called in previous calls and only adding new
    elements into the permutation.

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
    if len(permutation) == n:
        print(permutation)
    else:
        for i in range(0, n):
            if i in chosen:
                continue
            chosen.add(i)
            permutation.append(i)
            print_recursive_permutations(n, permutation, chosen)
            chosen.remove(i)
            permutation.pop()


def generate_recursive_permutations(
        n: int, permutation: list=[], chosen: set=set()) -> list[list]:
    if len(permutation) == n:
        return [[i for i in permutation]]
    permutations = []
    for i in range(0, n):
        if i in chosen:
            continue
        chosen.add(i)
        permutation.append(i)
        permutations += generate_recursive_permutations(n, permutation, chosen)
        chosen.remove(i)
        permutation.pop()
    return permutations


def generate_itertools_permutations(n: int) -> list[tuple]:
    return [
        p for p in permutations(range(n))
    ]


if __name__ == "__main__":
    print("We can print all recursive permutations")
    print_recursive_permutations(3)
    print("Or generate a list of all possible permutations")
    print(generate_recursive_permutations(3))
    print("Or just use itertools")
    print(generate_itertools_permutations(3))