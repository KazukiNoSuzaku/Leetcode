# Convert a non-negative integer num to its English words representation.

# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"

# Example 2:
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"

# Example 3:
# Input: num = 1000010
# Output: "One Million Ten"

# Constraints:
# 0 <= num <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
                "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
                "Seventeen","Eighteen","Nineteen"]
        tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return ones[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return ones[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        for i, t in enumerate(thousands):
            if num % 1000 != 0:
                res = helper(num % 1000) + (t + " " if t else "") + res
            num //= 1000
            if num == 0:
                break
        return res.strip()
