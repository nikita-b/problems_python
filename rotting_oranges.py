# https://leetcode.com/problems/rotting-oranges/
# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1 instead.

from typing import List


class Solution:
    def __init__(self):
        self.ROTTEN_ORANGE = 2
        self.FRESH_ORANGE = 1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = dict()
        rotten = []

        len_x = len(grid[0])
        len_y = len(grid)

        # Creating dict with fresh oranges and list with rotten oranges
        for x in range(len_x):
            for y in range(len_y):
                if grid[y][x] == self.ROTTEN_ORANGE:
                    rotten.append((y, x))
                elif grid[y][x] == self.FRESH_ORANGE:
                    fresh[(y, x)] = True

        result = 0
        next_rotten = []

        # if we have rotten oranges then we check fresh oranges around and replace it to rotten
        while True:
            for y, x in rotten:
                for i, j in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if (i, j) in fresh:
                        del fresh[(i, j)]  # also, we can change the value to False and check it in the last expression
                        next_rotten.append((i, j))
            rotten = next_rotten[:]  # it's expensive operation. I believe we can use one list and slice
            next_rotten = []

            if not rotten:
                if fresh:
                    return -1
                else:
                    return result

            result += 1
