# You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order.
# Apply the following algorithm until arr contains only one number:
# Pick either from the left or right end of the list, remove that number, and add it to results.
# Alternate from left to right then right to left.
# Return the last number that remains in arr.

# Author: Kaustav Ghosh

class Solution(object):
    def lastRemaining(self, n):
        left = True
        head = 1
        step = 1
        remaining = n
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
        return head
