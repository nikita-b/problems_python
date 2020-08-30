# Given an array of integers A, We need to sort the array performing a series of pancake flips.
#
# In one pancake flip we do the following steps:
#
#     Choose an integer k where 0 <= k < A.length.
#     Reverse the sub-array A[0...k].
#
# For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1], so A = [1,2,3,4] after the pancake flip at k = 2.
#
# Return an array of the k-values of the pancake flips that should be performed in order to sort A. Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.
# https://leetcode.com/problems/pancake-sorting/

# This solution has couple of problem:
# 1. Need just swap elements instead creating new List
# 2. Sometimes we don't need to move elements

from typing import List

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        left = len(A)
        answer = []
        for i in range(1, len(A) + 1)[::-1]:
            buf = []
            for index, value in enumerate(A):
                buf.append(value)
                if value == i:
                    if index != 0:
                        A = buf[::-1] + A[index + 1:]
                        answer.append(index + 1)
                    answer.append(left)
                    A = A[:left][::-1]
                    left -= 1
                    break

        return answer[:-1]

