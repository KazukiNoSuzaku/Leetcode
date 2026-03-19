# Author: Kaustav Ghosh
# https://leetcode.com/problems/average-waiting-time/

class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        current_time = 0
        total_wait = 0
        for arrival, time in customers:
            current_time = max(current_time, arrival) + time
            total_wait += current_time - arrival
        return total_wait / float(len(customers))
