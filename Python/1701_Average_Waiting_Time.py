# Author: Kaustav Ghosh
# Problem: Average Waiting Time
# Approach: Serve customers in order; the chef starts each order at max(free time, arrival), and waiting is finish - arrival

class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        free = 0
        total_wait = 0
        for arrival, time in customers:
            free = max(free, arrival) + time
            total_wait += free - arrival
        return total_wait / float(len(customers))
