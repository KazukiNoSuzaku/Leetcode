# Author: Kaustav Ghosh
# Problem: Maximum Score From Removing Substrings
# Approach: Greedily strip the higher-scoring pair first with a stack, then strip the other from what remains; taking the cheaper pair first can never help

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def strip(text, first, second, gain):
            stack = []
            score = 0
            for c in text:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    score += gain
                else:
                    stack.append(c)
            return ''.join(stack), score

        if x >= y:
            s, first_score = strip(s, 'a', 'b', x)
            s, second_score = strip(s, 'b', 'a', y)
        else:
            s, first_score = strip(s, 'b', 'a', y)
            s, second_score = strip(s, 'a', 'b', x)
        return first_score + second_score
