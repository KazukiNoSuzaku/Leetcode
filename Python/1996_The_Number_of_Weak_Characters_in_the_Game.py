# Author: Kaustav Ghosh
# Problem: The Number of Weak Characters in the Game
# Approach: Sorting by attack descending removes one of the two comparisons, because every character seen earlier already has an attack at least as large. Ordering the ties by defence ascending is what makes the remaining comparison exact: characters with equal attack are then scanned weakest defence first, so the running maximum defence only reflects characters whose attack is strictly greater by the time a character is examined. A character is weak precisely when its defence falls below that running maximum, so one sort and one pass suffice.

class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        ordered = sorted(properties, key=lambda pair: (-pair[0], pair[1]))
        strongest = 0
        weak = 0
        for _, defense in ordered:
            if defense < strongest:
                weak += 1
            elif defense > strongest:
                strongest = defense
        return weak
