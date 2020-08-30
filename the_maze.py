# There is a ball in a maze with empty spaces and walls.
# The ball can go through empty spaces by rolling up, down, left or right,
# but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze,
# determine whether the ball could stop at the destination.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
# You may assume that the borders of the maze are all walls.
# The start and destination coordinates are represented by row and column indexes.
# https://leetcode.com/problems/the-maze/

from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.result = False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Generating borders. It'll be ineffective. but it'll be easier for us
        start = [start[0] + 1, start[1] + 1]
        destination = [destination[0] + 1, destination[1] + 1]
        top_down_border = [1, ] * (len(maze[0]) + 2)

        real_maze = [top_down_border.copy()]

        for y in maze:
            real_maze.append([1, ] + y + [1, ])

        real_maze.append(top_down_border.copy())

        def flow(current: List) -> None:
            if self.result or current in self.visited:
                return

            self.visited.add(current)

            if list(current) == destination:
                self.result = True

            for change_x, change_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                step = False
                buf_current = current
                while True:
                    prev = buf_current
                    buf_current = (buf_current[0] + change_x, buf_current[1] + change_y)

                    if real_maze[buf_current[0]][buf_current[1]] == 1:
                        if step:
                            flow(prev)
                        break
                    else:
                        step = True

        flow(tuple(start))
        return self.result
