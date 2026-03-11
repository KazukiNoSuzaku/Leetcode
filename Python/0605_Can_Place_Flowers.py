# You have a long flowerbed with no flowers. Flowers cannot be planted in adjacent plots.
# Given a flowerbed array and a number n, return true if n flowers can be planted.

# Author: Kaustav Ghosh

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0 or flowerbed[i-1] == 0)
                right = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
