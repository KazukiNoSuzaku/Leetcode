# Author: Kaustav Ghosh
# Problem: Maximize the Confusion of an Exam
# Approach: For a target letter, the longest achievable run is the longest window containing at most k of the other letter (those get flipped). Slide a window per target and take the larger result

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def longest(target):
            left = 0
            other = 0
            best = 0
            for right, ch in enumerate(answerKey):
                if ch != target:
                    other += 1
                while other > k:
                    if answerKey[left] != target:
                        other -= 1
                    left += 1
                best = max(best, right - left + 1)
            return best

        return max(longest('T'), longest('F'))
