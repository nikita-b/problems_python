from typing import List
from functools import lru_cache
from math import inf

class Solution:
    def __init__(self):
        self.days = []
        self.dur_cost = []

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.dur_cost = zip((1, 7, 30), costs)
        durations = [1, 7, 30]

        @lru_cache(None)
        def loop(day: int) -> int:
            if day >= len(days):
                return 0

            ans = inf
            current = day
            for c, d in zip(costs, durations):
                while current < len(days) and days[current] < days[day] + d:
                    current += 1
                ans = min(ans, loop(current) + c)

            return ans

        return loop(0)
