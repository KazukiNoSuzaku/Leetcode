# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# Author: Kaustav Ghosh

class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(combination, open_count, close_count):
            # Base case: if the combination is complete, add it to the result
            if len(combination) == 2 * n:
                result.append(combination)
                return
            
            # If we can add an opening parenthesis, do so and recurse
            if open_count < n:
                backtrack(combination + "(", open_count + 1, close_count)
            
            # If we can add a closing parenthesis, do so and recurse
            if close_count < open_count:
                backtrack(combination + ")", open_count, close_count + 1)
        
        result = []
        backtrack("", 0, 0)
        return result