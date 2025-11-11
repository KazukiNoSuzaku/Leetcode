# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

 

# Example 1:

# Input: n = 3, k = 3
# Output: "213"
# Example 2:

# Input: n = 4, k = 9
# Output: "2314"
# Example 3:

# Input: n = 3, k = 1
# Output: "123"
 

# Constraints:

# 1 <= n <= 9
# 1 <= k <= n!

# Author: Kaustav Ghosh

class Solution(object):
    def getPermutation(self, n, k):
        import math
        
        # Create a list of numbers to get permutations from
        numbers = [i for i in range(1, n + 1)]
        
        # Adjust k to be zero-indexed
        k -= 1
        
        # Initialize the result string
        result = ""
        
        # Loop to find each digit of the permutation
        for i in range(n, 0, -1):
            # Determine the factorial of (i-1)
            fact = math.factorial(i - 1)
            
            # Determine the index of the current digit
            index = k // fact
            
            # Append the digit to the result
            result += str(numbers[index])
            
            # Remove the used digit from the list
            numbers.pop(index)
            
            # Update k for the next iteration
            k %= fact
        
        return result