# Author: Kaustav Ghosh
# Problem 1849: Splitting a String Into Descending Consecutive Values

class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def backtrack(index, prev, count):
            if index == len(s):
                return count >= 2
            for end in range(index + 1, len(s) + 1):
                num = int(s[index:end])
                if prev == -1 or num == prev - 1:
                    if backtrack(end, num, count + 1):
                        return True
                if prev != -1 and num >= prev:
                    break
            return False

        return backtrack(0, -1, 0)
