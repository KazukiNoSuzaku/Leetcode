# Author: Kaustav Ghosh
# Problem: Removing Stars From a String
# Approach: Each star deletes the closest remaining character to its left, which is exactly a stack pop: push letters, pop on stars, and join what is left

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
