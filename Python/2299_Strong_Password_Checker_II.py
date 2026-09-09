# Author: Kaustav Ghosh
# Problem: Strong Password Checker II
# Approach: Verify all rules directly: at least 8 characters, contains a lowercase, an uppercase, a digit, and one of the allowed special characters, and no two adjacent characters are equal

class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False
        specials = set("!@#$%^&*()-+")
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in specials for c in password)
        no_adjacent = all(password[i] != password[i + 1] for i in range(len(password) - 1))
        return has_lower and has_upper and has_digit and has_special and no_adjacent
