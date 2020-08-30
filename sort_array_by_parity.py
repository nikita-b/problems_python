# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
# https://leetcode.com/problems/sort-array-by-parity/

from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result_even = []
        result_odd = []
        for i in A:
            if (i % 2) == 0:
                result_even.append(i)
            else:
                result_odd.append(i)
        result_even.extend(result_odd)
        return result_even

