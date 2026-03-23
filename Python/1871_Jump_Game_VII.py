# Author: Kaustav Ghosh
# Problem 1871: Jump Game VII

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[-1] == '1':
            return False
        reachable = [False] * n
        reachable[0] = True
        count = 0  # number of reachable positions in the window
        for i in range(1, n):
            if i >= minJump:
                count += 1 if reachable[i - minJump] else 0
            if i > maxJump:
                count -= 1 if reachable[i - maxJump - 1] else 0
            if count > 0 and s[i] == '0':
                reachable[i] = True
        return reachable[-1]
