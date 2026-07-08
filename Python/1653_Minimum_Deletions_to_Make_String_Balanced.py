# Author: Kaustav Ghosh
# Problem: Minimum Deletions to Make String Balanced
# Approach: Scan left to right; to keep an 'a' we must have deleted every 'b' before it, so track running b-count and take min(delete this a, delete prior b's)

class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        b_seen = 0
        deletions = 0
        for c in s:
            if c == 'b':
                b_seen += 1
            else:  # 'a': either delete it, or delete all preceding 'b's
                deletions = min(deletions + 1, b_seen)
        return deletions
