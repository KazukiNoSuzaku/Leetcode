class Solution:
    def splitNum(self, num: int) -> int:
        # Sort digits; interleave between two numbers to put smaller digits in higher places.
        digits = sorted(str(num))
        return int(''.join(digits[::2])) + int(''.join(digits[1::2]))
