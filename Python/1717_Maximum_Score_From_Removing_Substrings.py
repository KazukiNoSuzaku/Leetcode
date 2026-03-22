# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        # Greedily remove the higher-value pair first
        if x >= y:
            first, second = 'a', 'b'
            first_val, second_val = x, y
        else:
            first, second = 'b', 'a'
            first_val, second_val = y, x

        score = 0

        # First pass: remove higher value pair
        stack = []
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                score += first_val
            else:
                stack.append(ch)

        # Second pass: remove lower value pair
        stack2 = []
        for ch in stack:
            if stack2 and stack2[-1] == second and ch == first:
                stack2.pop()
                score += second_val
            else:
                stack2.append(ch)

        return score
