# Author: Kaustav Ghosh
# Problem: Minimum Cost to Set Cooking Time
# Approach: The target can be entered as minutes:seconds in up to two ways (the natural split, and borrowing 60 seconds from a minute). For each valid encoding, type the digit string (no leading zeros) tracking finger moves and pushes, and take the cheaper cost

class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        def cost(minutes, seconds):
            if minutes > 99 or minutes < 0 or seconds > 99 or seconds < 0:
                return float('inf')
            digits = str(minutes * 100 + seconds)
            finger = startAt
            total = 0
            for ch in digits:
                d = int(ch)
                if d != finger:
                    total += moveCost
                    finger = d
                total += pushCost
            return total

        m, s = targetSeconds // 60, targetSeconds % 60
        return min(cost(m, s), cost(m - 1, s + 60))
