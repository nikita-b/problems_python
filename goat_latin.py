# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, s: str) -> str:
        result = ''
        for idx, word in enumerate(s.split()):
            if word[0].lower() in ('a', 'e', 'i', 'o', 'u'):
                word = ' ' + word + 'ma'

            else:
                word = ' ' + word[1:] + word[0] + 'ma'

            result += word + 'a' * (idx + 1)

        return result[1:]
