# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the
# width and the height of an envelope. One envelope can fit into another if and only if both
# the width and height of one envelope are greater than the other envelope's width and height.
# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Example 1:
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

# Constraints:
# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5

# Author: Kaustav Ghosh

import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        # Sort by width asc, then height desc to prevent using same width twice
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = []
        for _, h in envelopes:
            pos = bisect.bisect_left(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
        return len(tails)
