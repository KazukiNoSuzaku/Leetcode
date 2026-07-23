# Author: Kaustav Ghosh
# Problem: Finding the Users Active Minutes
# Approach: Collect each user's distinct active minutes in a set; their UAM is that size, so bucket users by UAM into the answer array

from collections import defaultdict

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        minutes = defaultdict(set)
        for user, time in logs:
            minutes[user].add(time)

        answer = [0] * k
        for active in minutes.values():
            uam = len(active)
            if uam <= k:
                answer[uam - 1] += 1
        return answer
