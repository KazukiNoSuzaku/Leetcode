# Author: Kaustav Ghosh
# Bitmask words, enumerate submasks of each puzzle containing first letter

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        from collections import Counter

        word_masks = Counter()
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            word_masks[mask] += 1

        result = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            mask = 0
            for c in puzzle:
                mask |= 1 << (ord(c) - ord('a'))
            count = 0
            # Enumerate all submasks of mask that include first letter
            sub = mask
            while sub:
                if sub & first:
                    count += word_masks.get(sub, 0)
                sub = (sub - 1) & mask
            result.append(count)
        return result
