from typing import List
import random
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.points = []
        for rect in self.rects:
            x1, y1, x2, y2 = rect
            self.points.append((abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

    def pick(self) -> List[int]:
        rect = random.choices(self.rects, weights=self.points)

        x1, y1, x2, y2 = rect[0]
        return (random.randrange(x1, x2 + 1), random.randrange(y1, y2 + 1))


# if need check randomness
#from collections import defaultdict
#a = defaultdict(int)

#for i in range(1000000):
#    t = s.pick()
#    a[t] += 1

#for i in a:
#    print('{}: {}'.format(i, a[i]))