# Author: Kaustav Ghosh
# Problem 2086: Minimum Number of Food Buckets to Feed the Hamsters

class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        s = list(hamsters)
        n = len(s)
        buckets = 0
        i = 0
        while i < n:
            if s[i] == 'H':
                if i + 1 < n and s[i + 1] == '.':
                    # Place bucket to the right (greedy, covers more)
                    buckets += 1
                    i += 3  # Skip past the bucket and next hamster it may cover
                elif i - 1 >= 0 and s[i - 1] == '.':
                    buckets += 1
                    i += 1
                else:
                    return -1
            else:
                i += 1
        return buckets
