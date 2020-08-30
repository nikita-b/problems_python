from typing import List
from collections import Counter
import sys
class Solution:
    def __init__(self):
        self.timeline = []
        self.current_timeline = 0
        self.result = 0
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter()
        for i in tasks:
            counter[i] += 1

        for task, num in counter.most_common():
            for i in range(num):
                self.add_to_timeline(task)
                wait = n
                while wait != 0:
                    wait -= 1
                    self.add_to_timeline(None)

            self.current_timeline = 0

        print(self.timeline)
        return len(self.timeline)

    def add_to_timeline(self, value):
        print(value, self.timeline, self.current_timeline)
        try:
            if self.timeline[self.current_timeline] is not None:
                self.current_timeline += 1
                self.add_to_timeline(value)
            self.timeline[self.current_timeline] = value
            self.current_timeline += 1
        except IndexError as e:
            self.timeline.append(None)
            self.add_to_timeline(value)





s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))  # 8
print(s.leastInterval(["A","A","A","B","B","B"], 0))  # 6
print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)) # 16