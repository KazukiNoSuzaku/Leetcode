# Your task is to calculate a^b mod 1337 where a is a positive integer and b is an
# extremely large positive integer given in the form of an array.

# Example 1:
# Input: a = 2, b = [3]
# Output: 8

# Example 2:
# Input: a = 2, b = [1,0]
# Output: 1024

# Constraints:
# 1 <= a <= 2^31 - 1
# 1 <= b.length <= 2000
# 0 <= b[i] <= 9
# b does not contain leading zeros.

# Author: Kaustav Ghosh

class Solution(object):
    def superPow(self, a, b):
        MOD = 1337

        def powmod(base, exp, mod):
            result = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1:
                    result = result * base % mod
                base = base * base % mod
                exp //= 2
            return result

        res = 1
        for digit in b:
            res = powmod(res, 10, MOD) * powmod(a, digit, MOD) % MOD
        return res
