# Author: Kaustav Ghosh
# Problem: Average Waiting Time
# Approach: The chef serves strictly in arrival order, so there is nothing to schedule and the whole thing is a single forward sweep: the chef starts a customer's order either the moment they arrive or the moment the previous order finishes, whichever is later, and that customer's wait is the gap from their arrival to that finish. Carrying only the time the chef next becomes free is enough state, so no queue is needed.

class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        free_at = 0
        total_wait = 0
        for arrival, duration in customers:
            start = free_at if free_at > arrival else arrival
            free_at = start + duration
            total_wait += free_at - arrival
        return float(total_wait) / len(customers)
