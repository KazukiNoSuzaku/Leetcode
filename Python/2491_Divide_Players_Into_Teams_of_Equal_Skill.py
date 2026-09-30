# Author: Kaustav Ghosh
# Problem: Divide Players Into Teams of Equal Skill
# Approach: Every team must hit the same total, so after sorting, the weakest player has to pair with the strongest, the next weakest with the next strongest, and so on. Check each pair against that total and accumulate the products, bailing out as soon as a pair misses

class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        ordered = sorted(skill)
        target = ordered[0] + ordered[-1]
        total = 0
        for i in range(len(ordered) // 2):
            low, high = ordered[i], ordered[-1 - i]
            if low + high != target:
                return -1
            total += low * high
        return total
