# Author: Kaustav Ghosh
# Problem: Check If a String Can Break Another String
# Approach: Sort both strings, check if one dominates the other

class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a = sorted(s1)
        b = sorted(s2)
        return (all(a[i] >= b[i] for i in range(len(a))) or
                all(b[i] >= a[i] for i in range(len(a))))
