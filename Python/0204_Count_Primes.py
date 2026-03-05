# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0

# Constraints:
# 0 <= n <= 5 * 10^6

# Author: Kaustav Ghosh

class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        i = 2
        while i * i < n:
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
            i += 1
        return sum(is_prime)
