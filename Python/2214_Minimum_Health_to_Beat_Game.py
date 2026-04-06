# Author: Kaustav Ghosh
# Problem: 2214. Minimum Health to Beat Game
# URL: https://leetcode.com/problems/minimum-health-to-beat-game/
# Difficulty: Medium (Premium)
#
# Approach:
# The armor can be applied exactly once to any single attack, absorbing up
# to `armor` damage from that attack. To minimise total health needed, apply
# the armor to the attack with the highest damage (capped at armor value).
# Answer = sum(damage) - min(max(damage), armor) + 1
# (+1 because health must be > 0 after the last hit, i.e. we need at least 1
# health remaining, so we need sum - saved + 1 health to start).

class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        :type damage: list[int]
        :type armor: int
        :rtype: int
        """
        total = sum(damage)
        saved = min(max(damage), armor)
        return total - saved + 1
