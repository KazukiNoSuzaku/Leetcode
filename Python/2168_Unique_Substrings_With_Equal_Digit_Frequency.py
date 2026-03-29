# Author: Kaustav Ghosh
# Problem: 2168. Unique Substrings With Equal Digit Frequency
# URL: https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/
# Difficulty: Medium
# Note: Premium problem

# Approach:
# Use rolling hash to count distinct substrings where all digit frequencies are equal.
# For each substring s[i..j], check if all non-zero digit counts are the same.
# Use a hash set of (rolling_hash, frequency_tuple) to count unique valid substrings.
# Rolling hash with base and mod prevents hash collisions efficiently.

class Solution(object):
    def equalDigitFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        n = len(s)
        MOD = (1 << 61) - 1
        BASE = 131

        for i in range(n):
            freq = [0] * 10
            h = 0
            for j in range(i, n):
                d = int(s[j])
                freq[d] += 1
                h = (h * BASE + d + 1) % MOD
                counts = [c for c in freq if c > 0]
                if len(set(counts)) == 1:
                    seen.add(h)

        return len(seen)
