# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 10^4 for all given inputs.

# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"

# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"

# Example 3:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"

# Constraints:
# -2^31 <= numerator, denominator <= 2^31 - 1
# denominator != 0

# Author: Kaustav Ghosh

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        integer = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            return sign + str(integer)
        decimal = []
        seen = {}
        while remainder:
            if remainder in seen:
                decimal.insert(seen[remainder], '(')
                decimal.append(')')
                break
            seen[remainder] = len(decimal)
            remainder *= 10
            decimal.append(str(remainder // denominator))
            remainder %= denominator
        return sign + str(integer) + '.' + ''.join(decimal)
