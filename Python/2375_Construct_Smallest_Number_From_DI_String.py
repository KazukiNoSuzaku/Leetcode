# Author: Kaustav Ghosh
# Problem: Construct Smallest Number From DI String
# Approach: The digits 1..9 are used in order, so push the next digit onto a stack at every position and flush the stack whenever the pattern calls for an increase or the pattern ends. Flushing reverses exactly the stretch covered by a run of 'D', which is the smallest arrangement that satisfies it

class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        stack = []
        digits = []
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    digits.append(stack.pop())
        return "".join(digits)
