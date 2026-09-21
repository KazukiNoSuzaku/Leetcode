# Author: Kaustav Ghosh
# Problem: Sort the People
# Approach: The heights are distinct, so pair each height with its name and sort the pairs by height descending, keeping the names

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
