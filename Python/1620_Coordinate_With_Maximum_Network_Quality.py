# Author: Kaustav Ghosh
# Problem: Coordinate With Maximum Network Quality
# Approach: Moving away from the towers' bounding box increases the distance to every tower at once and so can never help, which pins an optimum inside that box; coordinates must also be non-negative and every tower lies at or below fifty, so sweeping the fifty-one by fifty-one grid of integer points covers everything. Reachability is tested on squared distances, keeping that part in exact integers, and the signal itself divides by one plus the true Euclidean distance rather than a rounded one. I take the floating-point quotient only as a first guess and then settle the floor exactly, since k is the right answer precisely when k squared times the squared distance is at most (q - k) squared, which is pure integer arithmetic. Sweeping x and then y upward means the first point reaching the best total is already the lexicographically smallest.

class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        reach = radius * radius
        best_quality = 0
        best_point = [0, 0]
        for x in range(51):
            for y in range(51):
                quality = 0
                for tx, ty, q in towers:
                    dx = tx - x
                    dy = ty - y
                    gap = dx * dx + dy * dy
                    if gap > reach:
                        continue
                    signal = int(q / (1.0 + gap ** 0.5))
                    # Correct the guess with an exact integer test, so that a
                    # quotient sitting on a whole number cannot be misrounded.
                    while signal > 0 and signal * signal * gap > (q - signal) ** 2:
                        signal -= 1
                    while signal < q and (signal + 1) ** 2 * gap <= (q - signal - 1) ** 2:
                        signal += 1
                    quality += signal
                if quality > best_quality:
                    best_quality = quality
                    best_point = [x, y]
        return best_point
