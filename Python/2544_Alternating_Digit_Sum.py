class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # Left-most digit gets +1, alternating sign for each subsequent digit.
        result = 0
        sign = 1
        for ch in str(n):
            result += sign * int(ch)
            sign = -sign
        return result
