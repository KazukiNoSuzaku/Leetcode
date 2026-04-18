# Author: Kaustav Ghosh
# 2337. Move Pieces to Obtain a String
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/
# Two pointers: L can only move left, R can only move right

class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        n = len(start)
        i = j = 0

        while i <= n and j <= n:
            # Skip blanks in both strings
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            # Both reached the end
            if i == n and j == n:
                return True
            # Only one reached the end
            if i == n or j == n:
                return False

            # Pieces must match
            if start[i] != target[j]:
                return False

            # L can only move left (i >= j means it can move from i to j)
            if start[i] == 'L' and i < j:
                return False
            # R can only move right (i <= j means it can move from i to j)
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True
