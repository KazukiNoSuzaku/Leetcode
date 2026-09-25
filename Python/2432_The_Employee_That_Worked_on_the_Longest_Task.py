# Author: Kaustav Ghosh
# Problem: The Employee That Worked on the Longest Task
# Approach: The logs are in order and each task runs from the previous leave time, so its length is the difference between consecutive leave times. Track the longest length seen, replacing it only on a strictly longer task so ties keep the smallest employee id

class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        best_id = logs[0][0]
        best_time = logs[0][1]
        previous = logs[0][1]
        for worker, leave in logs[1:]:
            duration = leave - previous
            if duration > best_time or (duration == best_time and worker < best_id):
                best_id, best_time = worker, duration
            previous = leave
        return best_id
