# Author: Kaustav Ghosh
# Problem: Minimum Number of Flips to Make the Binary String Alternating
# Approach: Moving the first character to the end is a rotation and costs nothing, so the real question is the cheapest rotation to make alternating, and every rotation of the string appears as a window of the original length inside the string concatenated with itself. Sliding that window and keeping the mismatches against the two alternating patterns, measured against absolute position parity, gives both costs at once; which of the two corresponds to starting with a zero depends on the window's parity, so taking the smaller of the pair covers both without tracking that. Each step admits one character and retires one, so the whole sweep is linear even though the string can be a hundred thousand long and of odd length, where the two patterns swap roles between rotations.

class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        doubled = s + s
        # Mismatch counts for the two patterns, keyed on absolute position:
        # one puts '0' on even positions, the other puts '1' there.
        zero_on_even = 0
        one_on_even = 0
        best = n
        for index, character in enumerate(doubled):
            if character == ("0" if index % 2 == 0 else "1"):
                one_on_even += 1
            else:
                zero_on_even += 1
            if index >= n:
                left = index - n
                if doubled[left] == ("0" if left % 2 == 0 else "1"):
                    one_on_even -= 1
                else:
                    zero_on_even -= 1
            if index >= n - 1:
                best = min(best, zero_on_even, one_on_even)
        return best
