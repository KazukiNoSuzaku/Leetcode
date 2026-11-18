# Author: Kaustav Ghosh
# Problem: Maximum Product of the Length of Two Palindromic Substrings
# Approach: The two substrings must not overlap, so the answer is the best split point: the longest odd palindrome lying entirely in the prefix, times the longest lying entirely in the suffix. Manacher's algorithm gives every centre's maximal odd radius in linear time, and from those radii I derive, for each position, the longest odd palindrome ending exactly there and the longest starting exactly there. The derivation uses the fact that stripping the two outer characters of a palindrome leaves a palindrome two shorter, so a maximal palindrome ending at a position implies one two shorter ending at the position before; propagating that backwards fills in every ending position, and the mirror-image propagation forwards fills every starting position. Running prefix and suffix maxima over those turn into the two factors, and one sweep over the split points finishes it, all in O(n) time.

class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        radius = [0] * length
        centre = 0
        reach = -1
        for index in range(length):
            span = 0
            if index <= reach:
                span = min(radius[2 * centre - index], reach - index)
            while (index - span - 1 >= 0 and index + span + 1 < length
                   and s[index - span - 1] == s[index + span + 1]):
                span += 1
            radius[index] = span
            if index + span > reach:
                centre = index
                reach = index + span

        ending = [1] * length
        for index in range(length):
            finish = index + radius[index]
            full = 2 * radius[index] + 1
            if full > ending[finish]:
                ending[finish] = full
        for index in range(length - 1, 0, -1):
            if ending[index] - 2 > ending[index - 1]:
                ending[index - 1] = ending[index] - 2

        starting = [1] * length
        for index in range(length):
            begin = index - radius[index]
            full = 2 * radius[index] + 1
            if full > starting[begin]:
                starting[begin] = full
        for index in range(length - 1):
            if starting[index] - 2 > starting[index + 1]:
                starting[index + 1] = starting[index] - 2

        prefix = [0] * length
        running = 0
        for index in range(length):
            if ending[index] > running:
                running = ending[index]
            prefix[index] = running

        suffix = [0] * length
        running = 0
        for index in range(length - 1, -1, -1):
            if starting[index] > running:
                running = starting[index]
            suffix[index] = running

        return max(prefix[index] * suffix[index + 1] for index in range(length - 1))
