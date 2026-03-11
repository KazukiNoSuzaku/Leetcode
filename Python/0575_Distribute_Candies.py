# Alice has n candies. She wants to distribute half of them to her brother Bob.
# Return the maximum number of different types of candies she can eat.

# Author: Kaustav Ghosh

class Solution(object):
    def distributeCandies(self, candyType):
        return min(len(set(candyType)), len(candyType) // 2)
