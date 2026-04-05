# Author: Kaustav Ghosh
# 2207. Maximize Number of Subsequences in a String
# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/
# Difficulty: Medium
#
# Approach: We can insert exactly one copy of pattern[0] or pattern[1] into text.
# - Insert pattern[0] at the very beginning: every existing pattern[1] in text
#   becomes a new valid subsequence. Gain = count of pattern[1] in text.
# - Insert pattern[1] at the very end: every existing pattern[0] in text
#   becomes a new valid subsequence. Gain = count of pattern[0] in text.
# Pick whichever insertion yields the higher gain, add it to the base count
# of pattern as a subsequence in the original text.
#
# Base count: scan left to right, track how many pattern[0] seen so far;
# each time we see pattern[1], add that running count.
# (If pattern[0] == pattern[1], each new char contributes running_count.)

class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        p0, p1 = pattern[0], pattern[1]

        # Count base subsequences and frequencies
        base = 0
        count0 = 0  # occurrences of p0 seen so far
        cnt0_total = 0
        cnt1_total = 0

        for ch in text:
            if ch == p0:
                count0 += 1
                cnt0_total += 1
            if ch == p1:
                base += count0
                cnt1_total += 1

        # Gain from inserting p0 at front = cnt1_total
        # Gain from inserting p1 at end   = cnt0_total
        gain = max(cnt1_total, cnt0_total)

        return base + gain
