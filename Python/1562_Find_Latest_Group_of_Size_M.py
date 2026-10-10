# Author: Kaustav Ghosh
# Problem: Find Latest Group of Size M
# Approach: Rather than rescanning the bit string each step, I keep for every run of ones its length recorded at both of its endpoints, so flipping a bit on lets me read the lengths of the runs immediately left and right of it in constant time, merge them into one run of left + right + 1, and write the new length back at the merged run's two ends; a tally of how many runs currently have each length then answers "does a run of exactly m exist" in constant time, and I remember the last step at which that tally was non-zero.

class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        n = len(arr)
        # length[p] is meaningful only when p is an endpoint of a run of ones.
        length = [0] * (n + 2)
        count = [0] * (n + 1)
        answer = -1
        for step, pos in enumerate(arr, 1):
            left = length[pos - 1]
            right = length[pos + 1]
            total = left + right + 1
            if left:
                count[left] -= 1
            if right:
                count[right] -= 1
            count[total] += 1
            length[pos - left] = total
            length[pos + right] = total
            if count[m]:
                answer = step
        return answer
