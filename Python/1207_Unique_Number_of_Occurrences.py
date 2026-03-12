# Author: Kaustav Ghosh
# Check if all value counts are distinct

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        count = Counter(arr)
        return len(count.values()) == len(set(count.values()))
