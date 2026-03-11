# You have a board of colored balls: a row of colored balls and a hand of balls.
# Return the minimum number of balls needed to clear all the balls on the board.
# If you cannot clear all the balls, return -1.

# Author: Kaustav Ghosh

from collections import Counter
import re

class Solution(object):
    def findMinStep(self, board, hand):
        hand_count = Counter(hand)

        def clean(s):
            while True:
                ns = re.sub(r'(.)\1{2,}', '', s)
                if ns == s:
                    return s
                s = ns

        def dfs(board, hand):
            board = clean(board)
            if not board:
                return 0
            res = float('inf')
            i = 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1
                needed = 3 - (j - i)
                if hand.get(board[i], 0) >= needed:
                    hand[board[i]] -= needed
                    sub = dfs(board[:i] + board[j:], hand)
                    if sub != -1:
                        res = min(res, needed + sub)
                    hand[board[i]] += needed
                i = j
            return res if res != float('inf') else -1

        return dfs(board, hand_count)
