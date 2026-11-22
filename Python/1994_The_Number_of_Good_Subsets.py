# Author: Kaustav Ghosh
# Problem: The Number of Good Subsets
# Approach: A product is the product of distinct primes exactly when every chosen value is squarefree and no two chosen values share a prime factor, so only the values 2 through 30 that are squarefree can ever appear and each contributes a fixed mask over the ten primes below 30. That turns the count into a subset-sum over masks: a table indexed by the set of primes already used is extended by every squarefree value, multiplying by how many copies of that value the array holds. Ones never change the product, so each is independently in or out and the final total is multiplied by two to the power of their count.

class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        counts = [0] * 31
        for value in nums:
            counts[value] += 1

        masks = {}
        for value in range(2, 31):
            if counts[value] == 0:
                continue
            mask = 0
            remaining = value
            squarefree = True
            for index, prime in enumerate(primes):
                if remaining % prime == 0:
                    remaining //= prime
                    mask |= 1 << index
                    if remaining % prime == 0:
                        squarefree = False
                        break
            if squarefree:
                masks[value] = mask

        ways = [0] * (1 << len(primes))
        ways[0] = 1
        for value, mask in masks.items():
            copies = counts[value]
            for used in range(len(ways) - 1, -1, -1):
                if ways[used] and used & mask == 0:
                    ways[used | mask] = (ways[used | mask] + ways[used] * copies) % MOD

        total = (sum(ways) - ways[0]) % MOD
        return total * pow(2, counts[1], MOD) % MOD
