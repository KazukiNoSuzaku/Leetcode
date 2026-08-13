# Author: Kaustav Ghosh
# Problem: Check if Word Can Be Placed In Crossword
# Approach: A placement occupies a maximal run of non-blocked cells bounded by '#' or edges. Collect those runs from every row and column, and for each run whose length matches the word, check whether the word (or its reverse) is compatible - each cell empty or equal to the letter

class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(word)

        def fits(slot):
            if len(slot) != n:
                return False
            forward = all(c == ' ' or c == w for c, w in zip(slot, word))
            backward = all(c == ' ' or c == w for c, w in zip(slot, word[::-1]))
            return forward or backward

        lines = [''.join(row) for row in board]
        lines += [''.join(col) for col in zip(*board)]

        for line in lines:
            for slot in line.split('#'):
                if fits(slot):
                    return True
        return False
