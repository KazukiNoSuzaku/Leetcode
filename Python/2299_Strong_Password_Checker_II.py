# Author: Kaustav Ghosh
# Problem: 2299. Strong Password Checker II
# URL: https://leetcode.com/problems/strong-password-checker-ii/
# Difficulty: Easy

class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        special = set("!@#$%^&*()-+")
        for i, c in enumerate(password):
            if c.islower():
                has_lower = True
            if c.isupper():
                has_upper = True
            if c.isdigit():
                has_digit = True
            if c in special:
                has_special = True
            if i > 0 and password[i] == password[i - 1]:
                return False
        return has_lower and has_upper and has_digit and has_special
