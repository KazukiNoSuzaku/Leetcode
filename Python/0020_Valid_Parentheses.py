# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Author: Kaustav Ghosh

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # If the stack is not empty, pop the top element
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly
        return not stack
        