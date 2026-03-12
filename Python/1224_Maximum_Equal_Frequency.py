# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Track frequency counts and check valid conditions at each prefix

class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        freq = defaultdict(int)
        max_freq = 0
        result = 0

        for i, num in enumerate(nums):
            if count[num] > 0:
                freq[count[num]] -= 1
                if freq[count[num]] == 0:
                    del freq[count[num]]
            count[num] += 1
            freq[count[num]] += 1
            max_freq = max(max_freq, count[num])
            n = i + 1

            if max_freq == 1:
                result = n
            elif len(freq) == 1 and max_freq * freq[max_freq] == n - 1 and max_freq > 1:
                result = n
            elif len(freq) == 1 and freq.get(1, 0) == n:
                result = n
            elif len(freq) == 2:
                keys = sorted(freq.keys())
                if keys[1] == keys[0] + 1 and freq[keys[1]] == 1:
                    result = n
                elif keys[0] == 1 and freq[keys[0]] == 1:
                    result = n
            elif max_freq * freq.get(max_freq, 0) == n - 1:
                result = n
        return result
