# Author: Kaustav Ghosh
# Problem: Maximum Number of People That Can Be Caught in Tag
# Approach: Scan the "it" people in index order and greedily assign each the earliest not-yet-caught target within [pos-dist, pos+dist]. A two-pointer over the target indices makes this optimal on a line

class Solution(object):
    def catchMaximumAmountofPeople(self, team, dist):
        """
        :type team: List[int]
        :type dist: int
        :rtype: int
        """
        zeros = [i for i, v in enumerate(team) if v == 0]
        count = 0
        j = 0
        for i, v in enumerate(team):
            if v != 1:
                continue
            while j < len(zeros) and zeros[j] < i - dist:
                j += 1
            if j < len(zeros) and zeros[j] <= i + dist:
                count += 1
                j += 1
        return count
