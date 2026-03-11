# Count numbers in [left, right] whose bit count is prime.

# Author: Kaustav Ghosh

class Solution(object):
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(n).count('1') in primes for n in range(left, right + 1))
