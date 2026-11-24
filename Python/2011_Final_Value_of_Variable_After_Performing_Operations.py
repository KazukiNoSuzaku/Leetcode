# Author: Kaustav Ghosh
# Problem: Final Value of Variable After Performing Operations
# Approach: Each operation moves the variable by exactly one, and whether it moves up or down is decided solely by which sign the operation carries, not by whether the sign sits before or after the variable. So the position of the plus or minus in the string is irrelevant and the whole sequence collapses to a count: every operation containing a plus contributes one upward and every other contributes one downward. Summing those contributions in a single pass gives the final value without ever simulating the variable.

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return sum(1 if '+' in operation else -1 for operation in operations)
