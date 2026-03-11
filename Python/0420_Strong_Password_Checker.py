# A password is considered strong if:
# - Length is at least 6 and at most 20.
# - Contains at least one lowercase letter, uppercase letter, and digit.
# - Does not contain 3 or more repeating characters in a row.
# Given a string password, return the minimum number of steps to make it strong.

# Author: Kaustav Ghosh

class Solution(object):
    def strongPasswordChecker(self, password):
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing = (not has_lower) + (not has_upper) + (not has_digit)

        # Find repeating groups
        repeats = []
        i = 2
        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                while i < n and password[i] == password[i-1]:
                    length += 1
                    i += 1
                repeats.append(length)
            else:
                i += 1

        if n < 6:
            return max(missing, 6 - n)
        elif n <= 20:
            replace = sum(r // 3 for r in repeats)
            return max(missing, replace)
        else:
            # Need to delete (n - 20) characters
            delete = n - 20
            # Optimize: delete from repeats to reduce replacements
            for mod in range(3):
                for idx in range(len(repeats)):
                    if repeats[idx] % 3 == mod and delete > mod:
                        d = mod + 1
                        repeats[idx] -= d
                        delete -= d
            replace = sum(r // 3 for r in repeats)
            return (n - 20) + max(missing, replace)
