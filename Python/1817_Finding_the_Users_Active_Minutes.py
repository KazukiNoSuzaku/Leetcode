# Author: Kaustav Ghosh

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        user_mins = defaultdict(set)
        for uid, minute in logs:
            user_mins[uid].add(minute)
        ans = [0] * k
        for uid, mins in user_mins.items():
            uam = len(mins)
            if uam <= k:
                ans[uam - 1] += 1
        return ans
