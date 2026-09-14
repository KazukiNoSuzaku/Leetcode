# Author: Kaustav Ghosh
# Problem: Minimum Amount of Time to Fill Cups
# Approach: Each second fills at most two cups of different types. If the largest count is at least the other two combined, every second must include it, taking max(amount) seconds; otherwise the cups can be paired off almost perfectly, taking ceil(total / 2). The answer is the larger of the two bounds

class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        return max(max(amount), (sum(amount) + 1) // 2)
