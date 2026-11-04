# Author: Kaustav Ghosh
# Problem: Finding the Users Active Minutes
# Approach: Several actions inside the same minute count once, so each user's minutes are gathered into a set, which removes the repeats as the log is read. The answer is then a tally of how many users ended up with each set size, and because the buckets run from one to k the counts drop straight into a list of that length without any sorting.

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict

        minutes = defaultdict(set)
        for user, minute in logs:
            minutes[user].add(minute)

        answer = [0] * k
        for seen in minutes.values():
            answer[len(seen) - 1] += 1
        return answer
