# Author: Kaustav Ghosh
# Problem: Goal Parser Interpretation
# Approach: The three tokens are unambiguous and none is a prefix of another in a way that could be misread, since "(al)" always starts with an opening bracket followed by a letter while "()" has its closing bracket immediately, so a left-to-right scan can decide each token from the next one or two characters alone. Translating "()" to a single letter and "(al)" to its two letters leaves everything else to pass through unchanged.

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        pieces = []
        i = 0
        n = len(command)
        while i < n:
            if command[i] == 'G':
                pieces.append('G')
                i += 1
            elif command[i + 1] == ')':
                pieces.append('o')
                i += 2
            else:
                pieces.append('al')
                i += 4
        return ''.join(pieces)
