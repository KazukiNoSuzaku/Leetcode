# Author: Kaustav Ghosh
# Problem: Using a Robot to Print the Lexicographically Smallest String
# Approach: The robot's holding area is a stack, so the question is when to pop. Precompute the smallest character remaining in the unread part of s; popping the top is right exactly while it is no larger than anything still to come, since nothing later could be printed sooner

class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        smallest_ahead = [chr(127)] * (n + 1)
        for i in range(n - 1, -1, -1):
            smallest_ahead[i] = min(s[i], smallest_ahead[i + 1])
        stack = []
        printed = []
        for i, ch in enumerate(s):
            stack.append(ch)
            while stack and stack[-1] <= smallest_ahead[i + 1]:
                printed.append(stack.pop())
        printed.extend(reversed(stack))
        return "".join(printed)
