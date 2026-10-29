# Author: Kaustav Ghosh
# Problem: Can You Eat Your Favorite Candy on Your Favorite Day?
# Approach: Candies must be eaten in type order, so by the end of a given day the number consumed lies in a known band: at least one per day, since a candy must be eaten daily, and at most the daily cap per day. The favourite type occupies a fixed stretch of the overall ordering, found from a prefix total, and reaching it on that day is possible exactly when the two ranges overlap: the greediest pace must get past everything before the favourite type, and the slowest pace must not already be past the end of it. Both tests are a single comparison once the prefix totals are built, so each query is constant time.

class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prefix = [0] * (len(candiesCount) + 1)
        for i, count in enumerate(candiesCount):
            prefix[i + 1] = prefix[i] + count

        answers = []
        for favouriteType, favouriteDay, dailyCap in queries:
            days = favouriteDay + 1
            most = days * dailyCap
            least = days
            answers.append(most > prefix[favouriteType] and least <= prefix[favouriteType + 1])
        return answers
