# Author: Kaustav Ghosh
# https://leetcode.com/problems/goal-parser-interpretation/

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace('()', 'o').replace('(al)', 'al')
