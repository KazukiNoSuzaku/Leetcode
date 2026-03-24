# Author: Kaustav Ghosh
# Problem 1996: The Number of Weak Characters in the Game

class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        # Sort by attack descending, then defense ascending
        properties.sort(key=lambda x: (-x[0], x[1]))
        count = 0
        max_def = 0
        for _, defense in properties:
            if defense < max_def:
                count += 1
            else:
                max_def = defense
        return count
