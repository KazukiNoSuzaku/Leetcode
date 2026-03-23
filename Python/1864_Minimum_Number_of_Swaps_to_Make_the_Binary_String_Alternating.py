# Author: Kaustav Ghosh
# Problem 1864: Minimum Number of Swaps to Make the Binary String Alternating

class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')
        zeros = len(s) - ones
        if abs(ones - zeros) > 1:
            return -1

        def count_mismatches(start):
            # start=0 means pattern starts with '0', start=1 means starts with '1'
            mismatches = 0
            for i in range(len(s)):
                expected = (start + i) % 2
                if int(s[i]) != expected:
                    mismatches += 1
            return mismatches // 2

        if ones > zeros:
            return count_mismatches(1)
        elif zeros > ones:
            return count_mismatches(0)
        else:
            return min(count_mismatches(0), count_mismatches(1))
