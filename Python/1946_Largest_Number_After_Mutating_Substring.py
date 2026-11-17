# Author: Kaustav Ghosh
# Problem: Largest Number After Mutating Substring
# Approach: The number keeps its length, so it is largest when the earliest digit that can be raised is raised, which fixes where the mutated substring must begin: the first position whose digit maps to something strictly larger. From there the substring should keep extending while the mapping does not hurt, that is while each digit maps to something at least as large, because stopping early can only leave a later digit unimproved and extending past a digit that maps smaller would lower a more significant place than anything gained afterwards. So I scan once for that start, then continue mutating until the mapping would decrease a digit, and return the result, which is O(n) time.

class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        digits = [int(digit) for digit in num]
        started = False
        for index, digit in enumerate(digits):
            mapped = change[digit]
            if started:
                if mapped < digit:
                    break
                digits[index] = mapped
            elif mapped > digit:
                started = True
                digits[index] = mapped
        return "".join(str(digit) for digit in digits)
