# Author: Kaustav Ghosh
# Count balanced splits when running R count equals L count

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        balance = 0
        for ch in s:
            balance += 1 if ch == 'R' else -1
            if balance == 0:
                count += 1
        return count
