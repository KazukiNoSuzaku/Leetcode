# Author: Kaustav Ghosh
# Problem: Check if Numbers Are Ascending in a Sentence
# Approach: Pull out the numeric tokens in order and confirm each is strictly greater than the previous

class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = -1
        for token in s.split():
            if token.isdigit():
                num = int(token)
                if num <= prev:
                    return False
                prev = num
        return True
