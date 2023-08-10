"""Generate all subsets.

For example, the subsets of ``{0,1,2}`` are ``{}, {0}, {1}, {2}, {0,1},
{0,2}, {1,2}, {0,1,2}``. Two methods exist to explore all subsets: use
recursion, or use the bitwise representation.

Consider that these will generate all subsets for all natural numbers
including zero of size n. 
"""


def print_recursive_search(n: int, subset: list=[], k: int=0) -> None:
    if k == n:
        print(subset)
    else:
        print_recursive_search(n, subset, k + 1)
        subset.append(k)
        print_recursive_search(n, subset, k + 1)
        subset.pop()


def generate_recursive_search(
        n: int, subset: set=set(), k: int=0) -> list[set]:
    if k == n:
        # If we don't do a copy, which takes O(n), the remove function will
        # remove numbers from the solution
        return [subset.copy()]
    else:
        left_search = generate_recursive_search(n, subset, k + 1)
        subset.add(k)
        right_search = generate_recursive_search(n, subset, k + 1)
        subset.remove(k)
        return left_search + right_search


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
    print("First, print all generated subsets in the function")
    print_recursive_search(3)
    print("Then, generate an array of subsets and print everything")
    print(generate_recursive_search(3))
    print("But we can do the same with bits")
    print_bitwise_search(3)
    print("And we can get a useful list too")
    print(generate_bitwise_search(3))
