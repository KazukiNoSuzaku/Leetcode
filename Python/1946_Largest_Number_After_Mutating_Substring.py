# Author: Kaustav Ghosh
# Problem: Largest Number After Mutating Substring
# Approach: Scan left to right. Begin mutating at the first digit that the mapping strictly increases; once started, keep mutating while digits stay equal or larger, and stop at the first digit the mapping would shrink. This yields the largest number

class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        digits = list(num)
        started = False
        for i, ch in enumerate(digits):
            d = int(ch)
            nd = change[d]
            if nd > d:
                digits[i] = str(nd)
                started = True
            elif nd == d:
                if started:
                    digits[i] = str(nd)
            else:  # nd < d
                if started:
                    break
        return ''.join(digits)
