# Author: Kaustav Ghosh
# Problem: Minimum Health to Beat Game
# Approach: Health only decreases, so the tightest moment is after the last level; the minimum starting health is total damage minus the best armor saving, plus one. Armor is best spent on the highest-damage level, saving min(max(damage), armor)

class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        total = sum(damage)
        saved = min(max(damage), armor)
        return total - saved + 1
