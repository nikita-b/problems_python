# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# https://leetcode.com/problems/longest-palindrome/

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        c = Counter(s)

        for j in c:
            count += int(c[j] / 2) * 2

        if len(s) > count:
            count += 1

        return count
