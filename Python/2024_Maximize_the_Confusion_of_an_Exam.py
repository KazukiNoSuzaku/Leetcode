# Author: Kaustav Ghosh
# Problem 2024: Maximize the Confusion of an Exam

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def maxConsec(ch):
            left = 0
            count = 0
            result = 0
            for right in range(len(answerKey)):
                if answerKey[right] != ch:
                    count += 1
                while count > k:
                    if answerKey[left] != ch:
                        count -= 1
                    left += 1
                result = max(result, right - left + 1)
            return result

        return max(maxConsec('T'), maxConsec('F'))
