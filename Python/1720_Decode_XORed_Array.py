# Author: Kaustav Ghosh
# Problem: Decode XORed Array
# Approach: encoded[i] = arr[i] ^ arr[i+1], and XOR is its own inverse, so arr[i+1] = arr[i] ^ encoded[i] starting from first

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        for e in encoded:
            arr.append(arr[-1] ^ e)
        return arr
