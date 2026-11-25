# Author: Kaustav Ghosh
# Problem: Count Subarrays With More Ones Than Zeros
# Approach: Reading every zero as minus one turns the requirement into a subarray whose elements sum above zero, which happens exactly when the running total at the subarray's end exceeds the running total just before its start. So the count is the number of pairs of running totals where the later one is strictly larger. Rather than a search structure, the key observation is that the running total only ever moves by one, so the number of earlier totals strictly below the current one can be carried along: stepping up admits every earlier total equal to the old value, and stepping down discards every earlier total equal to the new value. A tally of how often each total has occurred supplies those two adjustments, leaving one linear pass.
# Note: the method name below reads the opposite way round from the problem title; that is
# the name LeetCode ships for this problem, so it is kept verbatim.

class Solution(object):
    def subarraysWithMoreZerosThanOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        MOD = 10 ** 9 + 7
        seen = defaultdict(int)
        seen[0] = 1
        running = 0
        below = 0
        answer = 0
        for value in nums:
            if value == 1:
                below += seen[running]
                running += 1
            else:
                below -= seen[running - 1]
                running -= 1
            answer += below
            seen[running] += 1
        return answer % MOD
