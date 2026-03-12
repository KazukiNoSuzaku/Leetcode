# Author: Kaustav Ghosh
# Greedy from both ends matching substrings

class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        count = 0
        left = 0
        right = n - 1
        l_str = ""
        r_str = ""
        while left < right:
            l_str += text[left]
            r_str = text[right] + r_str
            if l_str == r_str:
                count += 2
                l_str = ""
                r_str = ""
            left += 1
            right -= 1
        if left == right or l_str:
            count += 1
        return count
