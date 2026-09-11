# Author: Kaustav Ghosh
# Problem: Count Asterisks
# Approach: Bars '|' come in pairs delimiting excluded regions. Toggle an "inside" flag on each bar and count an asterisk only while outside a bar pair

class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        inside = False
        count = 0
        for ch in s:
            if ch == '|':
                inside = not inside
            elif ch == '*' and not inside:
                count += 1
        return count
