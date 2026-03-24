# Author: Kaustav Ghosh
# Problem 2018: Check if Word Can Be Placed In Crossword

class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        wlen = len(word)

        def check_slots(line):
            # Split by '#' and check each segment
            segment = []
            for ch in line:
                if ch == '#':
                    if len(segment) == wlen:
                        if all(s == ' ' or s == w for s, w in zip(segment, word)):
                            return True
                        if all(s == ' ' or s == w for s, w in zip(segment, word[::-1])):
                            return True
                    segment = []
                else:
                    segment.append(ch)
            if len(segment) == wlen:
                if all(s == ' ' or s == w for s, w in zip(segment, word)):
                    return True
                if all(s == ' ' or s == w for s, w in zip(segment, word[::-1])):
                    return True
            return False

        # Check rows
        for i in range(m):
            if check_slots(board[i]):
                return True

        # Check columns
        for j in range(n):
            col = [board[i][j] for i in range(m)]
            if check_slots(col):
                return True

        return False
