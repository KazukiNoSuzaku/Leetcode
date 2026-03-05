# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true

# Example 2:
# Input: n = 2
# Output: false

# Constraints:
# 1 <= n <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def isHappy(self, n):
        def digit_square_sum(x):
            total = 0
            while x:
                d = x % 10
                total += d * d
                x //= 10
            return total
        slow = fast = n
        while True:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(digit_square_sum(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
