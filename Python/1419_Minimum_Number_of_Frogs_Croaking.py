# Author: Kaustav Ghosh
# Problem: Minimum Number of Frogs Croaking
# Approach: Track in-progress croak sequences at each stage

class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        stages = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        count = [0] * 5
        max_frogs = 0
        for ch in croakOfFrogs:
            idx = stages[ch]
            if idx == 0:
                count[0] += 1
                max_frogs = max(max_frogs, count[0])
            else:
                if count[idx - 1] == 0:
                    return -1
                count[idx - 1] -= 1
                count[idx] += 1
            if idx == 4:
                count[4] -= 1
        if any(count[i] > 0 for i in range(4)):
            return -1
        return max_frogs
