# Author: Kaustav Ghosh
# Problem: Sum Game
# Approach: Only two quantities matter: the difference between the two halves' known digit sums, and how the question marks are split between them. If the total number of question marks is odd then Alice moves last and can always break any balance, so she wins outright. Otherwise the blanks pair up, and the right way to see it is that each pair of blanks in the same half is worth nine to whoever controls it: Bob answers a nine with a zero and a zero with a nine, so a surplus of blanks on one side is worth exactly nine for every two of them. Bob can therefore force equality precisely when the known difference already cancels that surplus, and Alice wins in every other case.

class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        half = len(num) // 2

        def tally(part):
            known = sum(int(c) for c in part if c != "?")
            return known, part.count("?")

        first_sum, first_blanks = tally(num[:half])
        second_sum, second_blanks = tally(num[half:])

        if (first_blanks + second_blanks) % 2:
            return True
        surplus = (second_blanks - first_blanks) // 2
        return first_sum - second_sum != surplus * 9
