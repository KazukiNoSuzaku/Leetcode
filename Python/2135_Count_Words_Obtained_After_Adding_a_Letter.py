# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        seen = set()
        for word in startWords:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            seen.add(mask)

        count = 0
        for word in targetWords:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            for ch in word:
                candidate = mask ^ (1 << (ord(ch) - ord('a')))
                if candidate in seen:
                    count += 1
                    break
        return count
