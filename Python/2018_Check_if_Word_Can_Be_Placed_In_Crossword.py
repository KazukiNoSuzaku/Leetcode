# Author: Kaustav Ghosh
# Problem: Check if Word Can Be Placed In Crossword
# Approach: A placement must fill a maximal run of non-blocked cells exactly, because leaving a free cell at either end of the run would put a space immediately before or after the word, so the only candidate slots are the runs between blocked cells whose length equals the word's. Each row and each column is scanned once, splitting it into those runs, and a run of the right length is tested against the word read forwards and read backwards, since the word may be placed in either direction. A cell matches when it is empty or already holds the required letter, and the first slot that accepts the word settles the answer.

class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        columns = len(board[0])
        width = len(word)
        backwards = word[::-1]

        def accepts(run):
            if len(run) != width:
                return False
            for candidate in (word, backwards):
                if all(cell == ' ' or cell == candidate[index]
                       for index, cell in enumerate(run)):
                    return True
            return False

        def scan(line):
            run = []
            for cell in line:
                if cell == '#':
                    if accepts(run):
                        return True
                    run = []
                else:
                    run.append(cell)
            return accepts(run)

        for row in board:
            if scan(row):
                return True
        for column in range(columns):
            if scan([board[row][column] for row in range(rows)]):
                return True
        return False
