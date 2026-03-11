# You have rods of given lengths. Attach some to make two equal supports.
# Return the tallest possible height of the supports (0 if not possible).

# Author: Kaustav Ghosh

class Solution(object):
    def tallestBillboard(self, rods):
        # dp[diff] = max height of taller side when difference between sides is diff
        dp = {0: 0}
        for r in rods:
            ndp = dict(dp)
            for diff, taller in dp.items():
                shorter = taller - diff
                # add rod to taller side
                new_diff = diff + r
                ndp[new_diff] = max(ndp.get(new_diff, 0), taller + r)
                # add rod to shorter side
                if r >= diff:
                    new_diff2 = r - diff
                    ndp[new_diff2] = max(ndp.get(new_diff2, 0), shorter + r)
                else:
                    new_diff2 = diff - r
                    ndp[new_diff2] = max(ndp.get(new_diff2, 0), taller)
            dp = ndp
        return dp.get(0, 0)
