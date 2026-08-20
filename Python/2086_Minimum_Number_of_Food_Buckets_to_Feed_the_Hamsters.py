# Author: Kaustav Ghosh
# Problem: Minimum Number of Food Buckets to Feed the Hamsters
# Approach: Scan hamsters left to right. If the left neighbor already has a bucket, it is fed. Otherwise place a bucket to the right when possible (it may also feed the next hamster), else to the left; if neither is empty it is impossible

class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        street = list(hamsters)
        n = len(street)
        count = 0
        for i in range(n):
            if street[i] != 'H':
                continue
            if i > 0 and street[i - 1] == 'B':
                continue
            if i + 1 < n and street[i + 1] == '.':
                street[i + 1] = 'B'
                count += 1
            elif i > 0 and street[i - 1] == '.':
                street[i - 1] = 'B'
                count += 1
            else:
                return -1
        return count
