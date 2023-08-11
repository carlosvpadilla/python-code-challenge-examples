#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 


class PlaceQueens:
    """Calculate number of ways n queens can be placed on an n x n chessboard.
    
    Constraint: no two queens can attack each other.
    """
    columns: set
    top_bottom_diagonals: set
    bottom_top_diagonals: set
    count: int
    n: int


    def _queen_in_top_bottom_diagonal(self, x: int, y: int) -> int:
        return (x + y) in self.top_bottom_diagonals
    
    def _queen_in_bottom_top_diagonal(self, x: int, y: int) -> int:
        return (x - y + self.n - 1) in self.bottom_top_diagonals
    
    def _add_queen(self, x, y) -> None:
        self.columns.add(x)
        self.top_bottom_diagonals.add(x + y)
        self.bottom_top_diagonals.add(x - y + self.n - 1)
    
    def _remove_queen(self, x, y) -> None:
        if x in self.columns:
            self.columns.remove(x)
        if self._queen_in_top_bottom_diagonal(x, y):
            self.top_bottom_diagonals.remove(x + y)
        if self._queen_in_bottom_top_diagonal(x, y):
            self.bottom_top_diagonals.remove(x - y + self.n - 1)
    
    def _reset(self):
        self.columns = set()
        self.top_bottom_diagonals = set()
        self.bottom_top_diagonals = set()
        self.count = 0
        self.n = 0
    
    def _init_(self):
        self._reset()
    
    def _search(self, y: int) -> None:
        if y == self.n:
            self.count += 1
            return
        for x in range(self.n):
            if (
                x in self.columns
                or self._queen_in_top_bottom_diagonal(x, y)
                or self._queen_in_bottom_top_diagonal(x, y)
            ):
                continue
            self._add_queen(x, y)
            self._search(y+1)
            self._remove_queen(x, y)


    def search(self, n: int) -> int:
        self._reset()
        self.n = n
        self._search(0)
        return self.count


if __name__ == "__main__":
    pq = PlaceQueens()
    board_size = 4
    print(
        f"This is the number of ways {board_size} queens can be placed in a "
        f"{board_size}x{board_size} chessboard:")
    print(pq.search(board_size))
    board_size = 13
    print("But as the input increases, the algorithm becomes too slow.")
    print(f"This is what happens when n = {board_size}")
    print(pq.search(board_size))
    print("That was slow, wasn't it?")
