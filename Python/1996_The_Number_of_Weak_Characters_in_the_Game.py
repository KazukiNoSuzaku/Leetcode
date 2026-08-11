# Author: Kaustav Ghosh
# Problem: The Number of Weak Characters in the Game
# Approach: Sort by attack descending, breaking ties by defense ascending. Sweep while tracking the max defense seen. A character is weak if its defense is below that max, since any earlier character with a higher max defense also had strictly greater attack (ties in attack sort with lower defense first, so they never falsely trigger)

class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda p: (-p[0], p[1]))
        max_defense = 0
        weak = 0
        for _, defense in properties:
            if defense < max_defense:
                weak += 1
            else:
                max_defense = defense
        return weak
