# Author: Kaustav Ghosh
# Problem: Minimize the Maximum of Two Arrays
# Approach: Binary search the smallest ceiling n that can serve both arrays. Up to n there are n - n / divisor1 numbers the first array may use, n - n / divisor2 for the second, and n - n / lcm available in total, so a ceiling works when each array's pool covers its quota and the shared pool covers both

from math import gcd


class Solution(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        :type divisor1: int
        :type divisor2: int
        :type uniqueCnt1: int
        :type uniqueCnt2: int
        :rtype: int
        """
        both = divisor1 // gcd(divisor1, divisor2) * divisor2
        low, high = 1, (uniqueCnt1 + uniqueCnt2) * 2 + 2
        while low < high:
            mid = (low + high) // 2
            if (mid - mid // divisor1 >= uniqueCnt1
                    and mid - mid // divisor2 >= uniqueCnt2
                    and mid - mid // both >= uniqueCnt1 + uniqueCnt2):
                high = mid
            else:
                low = mid + 1
        return low
