# Author: Kaustav Ghosh
# Problem: Maximize the Confusion of an Exam
# Approach: A run of identical answers is produced by choosing which letter the run will consist of and then flipping everything in the window that disagrees, so the question becomes the longest window containing at most the allowed number of disagreeing characters. For a fixed target letter that is a sliding window: the right edge advances through the string spending budget on each disagreeing character, and whenever the budget goes negative the left edge advances until it is restored, so every window examined is affordable. Running this once for each of the two letters and taking the larger result covers both choices in linear time.

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def longest(target):
            left = 0
            budget = k
            best = 0
            for right in range(len(answerKey)):
                if answerKey[right] != target:
                    budget -= 1
                while budget < 0:
                    if answerKey[left] != target:
                        budget += 1
                    left += 1
                if right - left + 1 > best:
                    best = right - left + 1
            return best

        return max(longest('T'), longest('F'))
