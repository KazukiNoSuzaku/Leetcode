# Author: Kaustav Ghosh
# Problem: 1578 - Minimum Time to Make Rope Colorful
# Approach: For each group of same-color consecutive, keep max cost, remove rest

class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(colors):
            j = i
            group_sum = 0
            group_max = 0
            while j < len(colors) and colors[j] == colors[i]:
                group_sum += neededTime[j]
                group_max = max(group_max, neededTime[j])
                j += 1
            result += group_sum - group_max
            i = j
        return result
