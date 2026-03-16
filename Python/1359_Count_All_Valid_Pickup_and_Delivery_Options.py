# Author: Kaustav Ghosh
# Problem: Count All Valid Pickup and Delivery Options
# Approach: Math: for i-th order, (2i-1) slots to place delivery after pickup

class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        result = 1
        for i in range(2, n + 1):
            # (2i-1) choices for where to insert delivery, times i ways...
            # Actually: result *= i * (2*i - 1)
            result = result * i * (2 * i - 1) % MOD
        return result
