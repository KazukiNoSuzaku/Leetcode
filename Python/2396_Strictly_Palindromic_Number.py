class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # For any n >= 4, representation in base n-2 is always "12" (not palindrome)
        # So the answer is always False
        return False
