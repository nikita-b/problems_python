#  By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.
#
# On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.
# https://leetcode.com/problems/find-permutation/
from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        result, stack = [], []

        for ind, val in enumerate(s):
            stack.append(ind + 1)
            if val == 'D':
                continue

            stack.reverse()
            result.extend(stack)
            stack = []
        else:
            stack.reverse()
            result.extend(stack)

        return result
