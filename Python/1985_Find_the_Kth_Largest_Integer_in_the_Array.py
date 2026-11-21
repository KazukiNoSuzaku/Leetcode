# Author: Kaustav Ghosh
# Problem: Find the Kth Largest Integer in the Array
# Approach: The entries are decimal strings up to a hundred digits long, so comparing them as strings directly would order "9" above "10"; but since none of them carries a leading zero, a longer string is always the larger number, and among equal lengths plain lexicographic order agrees with numeric order digit by digit. So sorting by the pair of length and the string itself puts them in true numeric order without converting anything to an integer, which keeps every comparison to a length check plus at most one hundred character comparisons. Taking the k-th entry from the end of that sorted order gives the answer in O(n log n) comparisons.

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        ordered = sorted(nums, key=lambda text: (len(text), text))
        return ordered[len(ordered) - k]
