# Author: Kaustav Ghosh
# Problem: Determine Color of a Chessboard Square
# Approach: A chessboard alternates in both directions, so a square's colour depends only on whether its file and rank sum to an even or an odd number. Taking the letter's position from 'a' and the digit as written gives those two indices, and since a1 is black the square is white exactly when their sum is odd.

class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        file_index = ord(coordinates[0]) - ord("a")
        rank_index = int(coordinates[1]) - 1
        return (file_index + rank_index) % 2 == 1
