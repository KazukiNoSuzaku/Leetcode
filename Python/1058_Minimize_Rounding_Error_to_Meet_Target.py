# Author: Kaustav Ghosh
# 1058. Minimize Rounding Error to Meet Target
# https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

import math

class Solution(object):
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
        prices = [float(p) for p in prices]
        floor_sum = sum(int(p) for p in prices)
        if target < floor_sum or target > math.ceil(sum(prices)):
            return "-1"
        ceil_count = target - floor_sum
        # Sort by fractional part descending to pick which ones to ceil
        fracs = sorted([(p - int(p)) for p in prices], reverse=True)
        error = 0.0
        for i, frac in enumerate(fracs):
            if i < ceil_count:
                error += 1 - frac  # cost of ceiling
            else:
                error += frac  # cost of flooring
        return "{:.3f}".format(error)
