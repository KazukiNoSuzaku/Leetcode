# Author: Kaustav Ghosh
# Problem: Smallest K-Length Subsequence With Occurrences of a Letter
# Approach: Greedy monotonic stack for the lexicographically smallest length-k subsequence, with two feasibility guards while popping/pushing: keep enough characters left to still reach length k, and keep enough letter slots (plus remaining letters in the suffix) to reach the required repetition count

class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        n = len(s)
        remaining_letters = s.count(letter)   # letters in s[i:] during iteration i
        stack = []
        letters_in_stack = 0
        for i, c in enumerate(s):
            while stack and stack[-1] > c and (len(stack) - 1 + n - i) >= k \
                    and (stack[-1] != letter or letters_in_stack - 1 + remaining_letters >= repetition):
                removed = stack.pop()
                if removed == letter:
                    letters_in_stack -= 1
            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    letters_in_stack += 1
                elif k - len(stack) > repetition - letters_in_stack:
                    stack.append(c)
            if c == letter:
                remaining_letters -= 1
        return ''.join(stack)
