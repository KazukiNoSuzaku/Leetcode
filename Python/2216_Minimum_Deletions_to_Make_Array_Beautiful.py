# Author: Kaustav Ghosh
# Problem: Minimum Deletions to Make Array Beautiful
# Approach: Greedily scan while tracking the parity of the kept length. When starting a pair (even kept length) accept the element; when completing a pair (odd kept length) accept only if it differs from the pair's first element, otherwise delete it. Finally drop a trailing unpaired element to keep the length even

class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        deletions = 0
        keep_len = 0
        prev = None
        for x in nums:
            if keep_len % 2 == 0:
                # first element of a new pair
                prev = x
                keep_len += 1
            else:
                # second element of the pair
                if x == prev:
                    deletions += 1  # would form a bad pair; delete it
                else:
                    keep_len += 1
        if keep_len % 2 == 1:
            deletions += 1  # make the length even
        return deletions
