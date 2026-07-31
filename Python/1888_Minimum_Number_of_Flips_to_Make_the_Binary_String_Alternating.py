# Author: Kaustav Ghosh
# Problem: Minimum Number of Flips to Make the Binary String Alternating
# Approach: Moving the first char to the end is a rotation, so slide a length-n window over s+s. For each window count mismatches against both alternating patterns (indexed absolutely), maintained incrementally

class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        doubled = s + s

        diff_even0 = 0  # mismatches vs pattern where even absolute index is '0'
        diff_even1 = 0  # the complementary pattern
        best = n
        left = 0

        for right in range(len(doubled)):
            bit = int(doubled[right])
            if bit != right % 2:
                diff_even0 += 1
            else:
                diff_even1 += 1

            if right - left + 1 > n:
                lb = int(doubled[left])
                if lb != left % 2:
                    diff_even0 -= 1
                else:
                    diff_even1 -= 1
                left += 1

            if right - left + 1 == n:
                best = min(best, diff_even0, diff_even1)

        return best
