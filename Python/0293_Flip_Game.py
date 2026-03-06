# You are playing a Flip Game with your friend. You are given a string currentState that
# contains only '+' and '-'. In one move, you and your friend can choose any two consecutive "++"
# and flip them to "--".
# Return all the possible states of the string after one valid move.

# Example 1:
# Input: currentState = "++++"
# Output: ["--++","+--+","++--"]

# Example 2:
# Input: currentState = "+"
# Output: []

# Constraints:
# 1 <= currentState.length <= 500
# currentState[i] is either '+' or '-'.

# Author: Kaustav Ghosh

class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        res = []
        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i+1] == '+':
                res.append(currentState[:i] + '--' + currentState[i+2:])
        return res
