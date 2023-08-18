#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
from time import time
 

class SolveMaze:
    maze: list
    n: int
    amount_of_paths: int

    def _reset(self):
        self.maze = [
            [
                False for _ in range(self.n)
            ] for _ in range(self.n)
        ]
        self.amount_of_paths = 0

    def __init__(self, n: int):
        self.n = n
        self._reset()
    
    def _print_maze(self):
        print("MAZE")
        for row in self.maze:
            print(row)
        print("ENDMAZE")

    def _generate_not_optimized(self, x: int=0, y: int=0, visited_tiles: int=1) -> None:
        self.maze[y][x] = True
        if visited_tiles == self.n * self.n:
            if x == self.n - 1 and y == self.n - 1:
                self.amount_of_paths += 1
            self.maze[y][x] = False
            return
        
        if y > 0 and not self.maze[y-1][x]:
            self._generate_not_optimized(x, y-1, visited_tiles+1)
        if y < self.n - 1 and not self.maze[y+1][x]:
            self._generate_not_optimized(x, y+1, visited_tiles+1)
        if x > 0 and not self.maze[y][x-1]:
            self._generate_not_optimized(x-1, y, visited_tiles+1)
        if x < self.n - 1 and not self.maze[y][x+1]:
            self._generate_not_optimized(x+1, y, visited_tiles+1)

        self.maze[y][x] = False

    def generate_not_optimized(self) -> int:
        self._reset()
        self._generate_not_optimized()
        return self.amount_of_paths
    
    def _generate_opt_1(self, x: int=0, y: int=0, visited_tiles: int=1) -> None:
        self.maze[y][x] = True
        if visited_tiles == self.n * self.n:
            if x == self.n - 1 and y == self.n - 1:
                self.amount_of_paths += 1
            self.maze[y][x] = False
            return
        
        if x == 0 and y == 0:
            # Only generate down solution
            self._generate_opt_1(x, y+1, visited_tiles+1)
        else:
            if y > 0 and not self.maze[y-1][x]:
                self._generate_opt_1(x, y-1, visited_tiles+1)
            if y < self.n - 1 and not self.maze[y+1][x]:
                self._generate_opt_1(x, y+1, visited_tiles+1)
            if x > 0 and not self.maze[y][x-1]:
                self._generate_opt_1(x-1, y, visited_tiles+1)
            if x < self.n - 1 and not self.maze[y][x+1]:
                self._generate_opt_1(x+1, y, visited_tiles+1)

        self.maze[y][x] = False
    
    def generate_opt_1(self) -> int:
        self._reset()
        self._generate_opt_1()
        return self.amount_of_paths * 2
    
    def _generate_opt_2(self, x: int=0, y: int=0, visited_tiles: int=1) -> None:
        if x == self.n - 1 and y == self.n - 1 and visited_tiles < self.n * self.n:
            return
        self.maze[y][x] = True
        if visited_tiles == self.n * self.n:
            if x == self.n - 1 and y == self.n - 1:
                self.amount_of_paths += 1
            self.maze[y][x] = False
            return
        
        if x == 0 and y == 0:
            # Only generate down solution
            self._generate_opt_2(x, y+1, visited_tiles+1)
        else:
            if y > 0 and not self.maze[y-1][x]:
                self._generate_opt_2(x, y-1, visited_tiles+1)
            if y < self.n - 1 and not self.maze[y+1][x]:
                self._generate_opt_2(x, y+1, visited_tiles+1)
            if x > 0 and not self.maze[y][x-1]:
                self._generate_opt_2(x-1, y, visited_tiles+1)
            if x < self.n - 1 and not self.maze[y][x+1]:
                self._generate_opt_2(x+1, y, visited_tiles+1)

        self.maze[y][x] = False
    
    def generate_opt_2(self) -> int:
        self._reset()
        self._generate_opt_2()
        return self.amount_of_paths * 2
    
    def _generate_opt_3(self, x: int=0, y: int=0, visited_tiles: int=1) -> None:
        if x == self.n - 1 and y == self.n - 1 and visited_tiles < self.n * self.n:
            return
        self.maze[y][x] = True
        if visited_tiles == self.n * self.n:
            if x == self.n - 1 and y == self.n - 1:
                self.amount_of_paths += 1
            self.maze[y][x] = False
            return
        
        if x == 0 and y == 0:
            # Only generate down solution
            self._generate_opt_3(x, y+1, visited_tiles+1)
        else:
            if y > 0 and not self.maze[y-1][x] and not (
                    y - 1 == 0 and x > 0 and x < self.n - 1
                    and not self.maze[y-1][x-1] and not self.maze[y-1][x+1]):
                self._generate_opt_3(x, y-1, visited_tiles+1)
            if y < self.n - 1 and not self.maze[y+1][x] and not (
                    y + 1 == self.n - 1 and x > 0 and x < self.n - 1
                    and not self.maze[y+1][x-1] and not self.maze[y+1][x+1]):
                self._generate_opt_3(x, y+1, visited_tiles+1)
            if x > 0 and not self.maze[y][x-1] and not (
                    x - 1 == 0 and y > 0 and y < self.n - 1
                    and not self.maze[y+1][x-1] and not self.maze[y-1][x-1]):
                self._generate_opt_3(x-1, y, visited_tiles+1)
            if x < self.n - 1 and not self.maze[y][x+1] and not (
                    x + 1 == self.n - 1 and y > 0 and y < self.n - 1
                    and not self.maze[y+1][x+1] and not self.maze[y-1][x+1]):
                self._generate_opt_3(x+1, y, visited_tiles+1)

        self.maze[y][x] = False
    
    def generate_opt_3(self) -> int:
        self._reset()
        self._generate_opt_3()
        return self.amount_of_paths * 2
    
    def _generate_opt_4(self, x: int=0, y: int=0, visited_tiles: int=1) -> None:
        if x == self.n - 1 and y == self.n - 1 and visited_tiles < self.n * self.n:
            return
        self.maze[y][x] = True
        if visited_tiles == self.n * self.n:
            if x == self.n - 1 and y == self.n - 1:
                self.amount_of_paths += 1
            self.maze[y][x] = False
            return
        
        if x == 0 and y == 0:
            # Only generate down solution
            self._generate_opt_4(x, y+1, visited_tiles+1)
        else:
            if y > 0 and not self.maze[y-1][x] and not (
                    (y - 1 == 0 or self.maze[y-2][x]) and x > 0 and x < self.n - 1
                    and not self.maze[y-1][x-1] and not self.maze[y-1][x+1]):
                self._generate_opt_4(x, y-1, visited_tiles+1)
            if y < self.n - 1 and not self.maze[y+1][x] and not (
                    (y + 1 == self.n - 1 or self.maze[y+2][x]) and x > 0 and x < self.n - 1
                    and not self.maze[y+1][x-1] and not self.maze[y+1][x+1]):
                self._generate_opt_4(x, y+1, visited_tiles+1)
            if x > 0 and not self.maze[y][x-1] and not (
                    (x - 1 == 0 or self.maze[y][x-2]) and y > 0 and y < self.n - 1
                    and not self.maze[y+1][x-1] and not self.maze[y-1][x-1]):
                self._generate_opt_4(x-1, y, visited_tiles+1)
            if x < self.n - 1 and not self.maze[y][x+1] and not (
                    (x + 1 == self.n - 1 or self.maze[y][x+2]) and y > 0 and y < self.n - 1
                    and not self.maze[y+1][x+1] and not self.maze[y-1][x+1]):
                self._generate_opt_4(x+1, y, visited_tiles+1)

        self.maze[y][x] = False
    
    def generate_opt_4(self) -> int:
        self._reset()
        self._generate_opt_4()
        return self.amount_of_paths * 2


if __name__ == "__main__":
    maze_size = 6
    print(f"How about we solve a {maze_size}x{maze_size} maze?")
    sm = SolveMaze(maze_size)
    print(f"One can solve a {maze_size}x{maze_size} maze in this amount of "
          "ways:")
    start_time = time()
    print(sm.generate_not_optimized())
    execution_time = time() - start_time
    print(f"But that took {execution_time} seconds to execute!")
    print("Let's try something a bit more optimal. Instead of searching "
          "through the entire search space, just generate a downwards solution "
          "and multiply by 2")
    start_time = time()
    print(sm.generate_opt_1())
    execution_time = time() - start_time
    print(f"That took {execution_time} seconds to execute. Looking better. Now"
          ", we will prune solutions that reach the final tile too early.")
    start_time = time()
    print(sm.generate_opt_2())
    execution_time = time() - start_time
    print(f"That took {execution_time} seconds to execute. Now, if we hit a "
          "wall, and we can turn left and right, we have just divided the maze"
          " and we can't continue searching. Let's prune solutions this way.")
    start_time = time()
    print(sm.generate_opt_3())
    execution_time = time() - start_time
    print(f"That took {execution_time} seconds to execute. Better, right? "
          "What if we generalize this concept to not being able to move "
          "forward instead of just a wall?")
    start_time = time()
    print(sm.generate_opt_4())
    execution_time = time() - start_time
    print(f"That took {execution_time} seconds to execute.")
    print("Generally speaking, the more pruning we do, the faster runtimes "
          "we get.")
