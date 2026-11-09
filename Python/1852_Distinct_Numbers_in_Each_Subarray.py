# Author: Kaustav Ghosh
# Problem: Distinct Numbers in Each Subarray
# Approach: Moving the window one step changes only two things, the value entering on the right and the value leaving on the left, so a tally of the window's contents can be carried forward instead of rebuilt. The count of distinct values is then just the number of keys in that tally, which is why a value is deleted outright once its count reaches zero rather than being left behind as a zero entry; otherwise the key count would drift upwards and never recover.

class Solution(object):
    def distinctNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter

        window = Counter(nums[:k])
        answers = [len(window)]
        for index in range(k, len(nums)):
            window[nums[index]] += 1
            leaving = nums[index - k]
            window[leaving] -= 1
            if not window[leaving]:
                del window[leaving]
            answers.append(len(window))
        return answers
