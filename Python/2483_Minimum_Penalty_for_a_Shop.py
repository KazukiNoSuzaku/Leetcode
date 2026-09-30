# Author: Kaustav Ghosh
# Problem: Minimum Penalty for a Shop
# Approach: Start with the penalty for closing at hour 0, which is one for every customer who would have come. Moving the closing hour one step later drops that hour's customer from the penalty if there was one, and adds a penalty for staying open with nobody there. Track the running penalty and keep the earliest hour achieving the smallest value

class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        penalty = customers.count('Y')
        best_penalty = penalty
        best_hour = 0
        for hour, ch in enumerate(customers):
            penalty += 1 if ch == 'N' else -1
            if penalty < best_penalty:
                best_penalty = penalty
                best_hour = hour + 1
        return best_hour
