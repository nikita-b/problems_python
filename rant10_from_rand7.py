# Given a function rand7 which generates a uniform random integer in the range 1 to 7,
# write a function rand10 which generates a uniform random integer in the range 1 to 10.
#
# Do NOT use system's Math.random().
# https://leetcode.com/problems/implement-rand10-using-rand7/
class Solution:
    def rand10(self):
        result = []
        for i in range(0, 10):
            result.append(rand7())

        return (sum(result) % 11) + 1