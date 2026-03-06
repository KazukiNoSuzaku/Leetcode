# Given two strings low and high that represent two integers low and high where low <= high,
# return the count of strobogrammatic numbers in the range [low, high].

# Example 1:
# Input: low = "50", high = "100"
# Output: 3

# Constraints:
# 1 <= low.length, high.length <= 15

# Author: Kaustav Ghosh

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        def helper(n, total):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            middles = helper(n - 2, total)
            res = []
            for mid in middles:
                for a, b in [('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')]:
                    if n != total or a != '0':
                        res.append(a + mid + b)
            return res

        count = 0
        for length in range(len(low), len(high) + 1):
            for num in helper(length, length):
                if (len(num) == len(low) and num < low) or (len(num) == len(high) and num > high):
                    continue
                count += 1
        return count
