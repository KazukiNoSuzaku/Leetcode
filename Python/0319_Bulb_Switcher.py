# There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off
# every second bulb. On the third round, you toggle every third bulb (turning on if it's off
# or turning off if it's on). For the ith round, you toggle every i bulb.
# For the nth round, you only toggle the last bulb.
# Return the number of bulbs that are on after n rounds.

# Example 1:
# Input: n = 3
# Output: 1
# Explanation: Initial state: [off, off, off]
#              After round 1: [on, on, on]
#              After round 2: [on, off, on]
#              After round 3: [on, off, off]

# Constraints:
# 0 <= n <= 10^9

# Author: Kaustav Ghosh

import math

class Solution(object):
    def bulbSwitch(self, n):
        return int(math.sqrt(n))
