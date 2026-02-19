# A valid IP address consists of exactly four integers separated by single dots.
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# Given a string s containing only digits, return all possible valid IP addresses
# that can be formed by inserting dots into s.

# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Constraints:
# 1 <= s.length <= 20
# s consists of digits only.

# Author: Kaustav Ghosh

class Solution(object):
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts):
            if len(parts) == 4 and start == len(s):
                result.append('.'.join(parts))
                return
            if len(parts) == 4 or start == len(s):
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start + length]
                if len(segment) > 1 and segment[0] == '0':
                    break
                if int(segment) > 255:
                    break
                backtrack(start + length, parts + [segment])

        backtrack(0, [])
        return result
