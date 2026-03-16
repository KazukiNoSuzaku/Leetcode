# Author: Kaustav Ghosh
# Problem: Largest Multiple of Three
# Approach: Greedy using digit sum mod 3, remove smallest digits to make sum divisible by 3

class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        digits.sort(reverse=True)
        total = sum(digits)
        remainder = total % 3
        if remainder == 0:
            result = ''.join(map(str, digits))
            return result.lstrip('0') or '0' if result else ''

        # Try removing one digit with same remainder
        mod1 = sorted([d for d in digits if d % 3 == 1])
        mod2 = sorted([d for d in digits if d % 3 == 2])

        if remainder == 1:
            if mod1:
                digits_copy = digits[:]
                digits_copy.remove(mod1[0])
                result = ''.join(map(str, digits_copy))
                if result:
                    return result.lstrip('0') or '0'
            if len(mod2) >= 2:
                digits_copy = digits[:]
                digits_copy.remove(mod2[0])
                digits_copy.remove(mod2[1])
                result = ''.join(map(str, digits_copy))
                if result:
                    return result.lstrip('0') or '0'
        else:
            if mod2:
                digits_copy = digits[:]
                digits_copy.remove(mod2[0])
                result = ''.join(map(str, digits_copy))
                if result:
                    return result.lstrip('0') or '0'
            if len(mod1) >= 2:
                digits_copy = digits[:]
                digits_copy.remove(mod1[0])
                digits_copy.remove(mod1[1])
                result = ''.join(map(str, digits_copy))
                if result:
                    return result.lstrip('0') or '0'

        return ""
