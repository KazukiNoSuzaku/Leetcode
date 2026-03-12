# Author: Kaustav Ghosh
# 1103. Distribute Candies to People
# https://leetcode.com/problems/distribute-candies-to-people/

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        result = [0] * num_people
        give = 1
        i = 0
        while candies > 0:
            result[i % num_people] += min(give, candies)
            candies -= give
            give += 1
            i += 1
        return result
