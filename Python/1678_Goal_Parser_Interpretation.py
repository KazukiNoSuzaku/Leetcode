# Author: Kaustav Ghosh
# Problem: Goal Parser Interpretation
# Approach: Replace the two multi-char tokens: "()" becomes "o" and "(al)" becomes "al"; "G" stays

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace('()', 'o').replace('(al)', 'al')
