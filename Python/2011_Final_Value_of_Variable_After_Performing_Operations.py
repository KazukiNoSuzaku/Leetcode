# Author: Kaustav Ghosh
# Problem: Final Value of Variable After Performing Operations
# Approach: Each operation shifts the variable by +1 or -1 depending on whether it contains a '+'. Sum those shifts

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return sum(1 if '+' in op else -1 for op in operations)
