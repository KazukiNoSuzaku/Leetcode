# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# Author: Kaustav Ghosh

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Result list
        result = []
    
        # Backtracking function
        def backtrack(index, path):
            # If the path is complete
            if index == len(digits):
                result.append("".join(path))
                return
            
            # Get the letters corresponding to the current digit
            letters = phone_map[digits[index]]
            for letter in letters:
                # Add the letter to the current path
                path.append(letter)
                # Move to the next digit
                backtrack(index + 1, path)
                # Backtrack and remove the letter from the current path
                path.pop()
    
        # Initialize backtracking
        backtrack(0, [])
        return result