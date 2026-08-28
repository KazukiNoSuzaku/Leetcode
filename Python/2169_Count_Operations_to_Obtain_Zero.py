# Author: Kaustav Ghosh
# Problem: Count Operations to Obtain Zero
# Approach: Each step subtracts the smaller from the larger. Batch consecutive subtractions with integer division (like the Euclidean algorithm) and accumulate the quotient as the operation count

class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        operations = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                operations += num1 // num2
                num1 %= num2
            else:
                operations += num2 // num1
                num2 %= num1
        return operations
