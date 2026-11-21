# Author: Kaustav Ghosh
# Problem: Number of Unique Good Subsequences
# Approach: A good subsequence either starts with '1' or is the single string "0", so I count the distinct subsequences beginning with '1' and add one at the end if the input contains any zero. Counting distinct subsequences, rather than distinct index choices, needs the state split by last character: keeping how many distinct good subsequences end in '0' and how many end in '1' makes each new character's effect exact, because appending that character to every existing subsequence produces exactly the subsequences ending in it, with no double counting from different index choices spelling the same string. So a '0' replaces the ends-in-zero count by the old total, and a '1' replaces the ends-in-one count by the old total plus one for the bare "1". One pass with two counters reduced modulo 10^9 + 7 gives O(n) time and constant space.

class Solution(object):
    def numberOfUniqueGoodSubsequences(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        ends_zero = 0
        ends_one = 0
        has_zero = False

        for bit in binary:
            if bit == '1':
                ends_one = (ends_zero + ends_one + 1) % MOD
            else:
                has_zero = True
                ends_zero = (ends_zero + ends_one) % MOD

        total = (ends_zero + ends_one) % MOD
        if has_zero:
            total = (total + 1) % MOD
        return total
