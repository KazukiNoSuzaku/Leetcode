# Maximize score: spend power to gain tokens, or spend tokens to gain power.

# Author: Kaustav Ghosh

class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        lo, hi = 0, len(tokens) - 1
        score = res = 0
        while lo <= hi:
            if power >= tokens[lo]:
                power -= tokens[lo]; score += 1; lo += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[hi]; score -= 1; hi -= 1
            else:
                break
        return res
