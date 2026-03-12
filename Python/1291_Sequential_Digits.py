# Author: Kaustav Ghosh
# Enumerate sequential digits from "123456789" using sliding window

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = "123456789"
        result = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(9 - length + 1):
                num = int(s[start:start + length])
                if low <= num <= high:
                    result.append(num)
        return result
