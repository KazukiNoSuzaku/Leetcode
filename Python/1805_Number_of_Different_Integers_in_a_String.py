# Author: Kaustav Ghosh

class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        nums = set()
        i = 0
        n = len(word)
        while i < n:
            if word[i].isdigit():
                j = i
                while j < n and word[j].isdigit():
                    j += 1
                nums.add(int(word[i:j]))
                i = j
            else:
                i += 1
        return len(nums)
