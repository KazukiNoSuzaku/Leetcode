# Author: Kaustav Ghosh
# Problem: Sum of Digits of String After Convert
# Approach: The conversion step is a direct character map, replacing each letter by its one-based alphabet position written out in decimal, so I build the converted number as a string by joining those positions rather than as an integer, which avoids any concern about the 100-letter input producing a value too large to write down conveniently. Each transform is then the sum of the decimal digits of the current value, so I compute the first sum straight off that string and the remaining k - 1 sums off the decimal spelling of the running total. After the very first transform the value is at most 9 * 200, so the later rounds are trivially small.

class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        digits = "".join(str(ord(letter) - ord('a') + 1) for letter in s)
        value = sum(int(digit) for digit in digits)
        for _ in range(k - 1):
            value = sum(int(digit) for digit in str(value))
        return value
