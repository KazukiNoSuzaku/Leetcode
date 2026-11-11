# Author: Kaustav Ghosh
# Problem: Jump Game VII
# Approach: A position is reachable when it holds a zero and at least one reachable position sits in the window from minJump to maxJump steps behind it, so the only thing the scan needs is how many reachable positions that window currently contains. Advancing one step admits exactly one position at the near edge and retires exactly one at the far edge, which keeps the count correct in constant time and avoids rescanning the window for every index. That turns what would be a quadratic sweep into a single pass over a hundred thousand characters.

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        inside = 0
        for index in range(1, n):
            if index >= minJump and reachable[index - minJump]:
                inside += 1
            if index > maxJump and reachable[index - maxJump - 1]:
                inside -= 1
            reachable[index] = inside > 0 and s[index] == "0"
        return reachable[-1]
