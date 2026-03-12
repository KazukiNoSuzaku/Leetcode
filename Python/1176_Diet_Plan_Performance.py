# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Sliding window sum compared to lower and upper thresholds

class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        points = 0
        window_sum = sum(calories[:k])
        if window_sum < lower:
            points -= 1
        elif window_sum > upper:
            points += 1
        for i in range(k, len(calories)):
            window_sum += calories[i] - calories[i - k]
            if window_sum < lower:
                points -= 1
            elif window_sum > upper:
                points += 1
        return points
