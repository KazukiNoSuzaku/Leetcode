# A magical string s consists of only '1' and '2' and obeys the following rules:
# The string s is magical because concatenating the number of contiguous occurrences of
# characters '1' and '2' generates the string s itself.
# Given an integer n, return the number of '1's in the first n number in the magical string s.

# Author: Kaustav Ghosh

class Solution(object):
    def magicalString(self, n):
        s = [1, 2, 2]
        head = 2
        while len(s) < n:
            s += [3 - s[-1]] * s[head]
            head += 1
        return s[:n].count(1)
