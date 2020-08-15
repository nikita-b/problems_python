# Given a collection of intervals, find the minimum number of intervals you need to remove to make
# the rest of the intervals non-overlapping.
# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])  # n log n

        result = 0
        old_start, old_end = None, None
        use_old = False
        for idn, value in enumerate(intervals):
            if idn + 1 >= len(intervals):
                break
            next_start, next_end = intervals[idn + 1]
            start, end = value
            if use_old:
                start, end = old_start, old_end
                use_old = False
            if end < next_start:
                continue
            elif end > next_start and end > next_end:
                result += 1
                continue
            elif end > next_start:
                result += 1
                use_old = True
                old_start, old_end = start, end

        return result
