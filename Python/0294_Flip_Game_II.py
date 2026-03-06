# You are playing a Flip Game with your friend. You are given a string currentState that
# contains only '+' and '-'. In one move, you can choose any two consecutive "++" and flip them to "--".
# The game ends when a person can no longer make a move. The person who cannot make a move loses.
# Given a string currentState, return true if the starting player can guarantee a win, false otherwise.

# Example 1:
# Input: currentState = "++++"
# Output: true

# Example 2:
# Input: currentState = "+"
# Output: false

# Constraints:
# 1 <= currentState.length <= 60

# Author: Kaustav Ghosh

class Solution(object):
    def canWin(self, currentState):
        memo = {}
        def can_win(s):
            if s in memo:
                return memo[s]
            for i in range(len(s) - 1):
                if s[i] == '+' and s[i+1] == '+':
                    next_s = s[:i] + '--' + s[i+2:]
                    if not can_win(next_s):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        return can_win(currentState)
