# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-good-meals/

class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        count = {}
        result = 0
        for val in deliciousness:
            for i in range(22):
                target = (1 << i) - val
                if target in count:
                    result = (result + count[target]) % MOD
            count[val] = count.get(val, 0) + 1
        return result
